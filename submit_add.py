import time
import socket
from funcx.sdk.client import FuncXClient

# 1. 初始化客户端
funcx_service_address = "http://36.103.203.228:32669/v1"
print(f"Connecting to Service at: {funcx_service_address}")

try:
    fxc = FuncXClient(funcx_service_address=funcx_service_address, force_login=False)
except TypeError:
    # 如果旧版SDK不支持force_login参数，则回退
    fxc = FuncXClient(funcx_service_address=funcx_service_address)

print("Client initialized.")

# 2. 定义函数
def add(a, b):
    import socket
    import os
    hostname = socket.gethostname()
    user = os.getenv('USER', 'unknown')
    return f"Hello! Running on host: '{hostname}' as user: '{user}' \nConputing result: {a+b}"

# 3. 注册函数
print("Start registering function")
try:
    func_uuid = fxc.register_function(add, searchable=False)
    print(f"Function UUID: {func_uuid}")
except Exception as e:
    print(f"Registration Failed: {e}")
    # 如果注册失败，通常是因为连不上 Web Service，或者鉴权头不对
    exit(1)

# 4. 提交任务
endpoint_id = "2cc6b8ac-6f12-444b-818f-dc00553b4222" # ep_test  (LocalProvider)
# endpoint_id = "96e12e24-6d29-4fd6-8c12-d9fe97c437ab" # ep_slurm (SlurmProvider)

a, b = 3, 8
print(f"Submitting task to Endpoint: {endpoint_id}")
print(f"Calling add({a}, {b})")

try:
    task_id = fxc.run(a, b, endpoint_id=endpoint_id, function_id=func_uuid)
    print(f"Task Submitted! ID: {task_id}")
except Exception as e:
    print(f"Submission Failed: {e}")
    exit(1)

# 5. 轮询结果
print("Waiting for result...")
start_time = time.time()
timeout = 1800

while True:
    if time.time() - start_time > timeout:
        print("\nTimed out waiting for result.")
        break

    try:
        result = fxc.get_result(task_id)
        print(f"\nSUCCESS! Result Received: \n{result}")
        break
    except Exception as e:
        # 兼容旧版 SDK 的 Pending 异常
        msg = str(e).lower()
        if "pending" in msg or "waiting" in msg or "not available" in msg:
            print(".", end="", flush=True)
            time.sleep(5)
        else:
            print(f"\nUnexpected Error: {e}")
            time.sleep(5)