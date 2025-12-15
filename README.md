# funcx-deployment
Private deployment based on the latest funcx source code.

## 项目结构
```text
funcx-deployment/
├── README.md  (说明文档)
├── funcx_sdk/ (修改后的 funcx-sdk 代码)
└── funcx_endpoint/ (修改后的 funcx-endpoint 代码)
```


## 部署说明书

本项目包含经过私有化改造的 `funcx` 和 `funcx-endpoint` 源码（基于 v0.3.5），已去除了 Globus 鉴权并适配了本地通信。

**请务必按照以下方式安装，不要使用 `pip install funcx`，否则会从官方源下载未修改的版本**

### 1\. 安装 Client (SDK)

在客户端机器（如 Mac/PC）上运行：

```bash
git clone https://github.com/QiaosunJoe/funcx-deployment.git
cd funcx-deployment/funcx_sdk
pip install . 
```

- `pip install .` 会读取当前目录的 `setup.py` 进行安装

### 2\. 安装 Endpoint

在执行端机器（如超算登录节点/Linux系统计算节点）上运行：

```bash
git clone https://github.com/QiaosunJoe/funcx-deployment.git
cd funcx-deployment/funcx_endpoint
pip install .
```

#### 3\. 验证安装

安装完成后，可以通过以下命令检查是否安装了我们的修改版：

```bash
pip show funcx
pip show funcx-endpoint
```
