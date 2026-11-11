# U2Net 抠图

自动去除图片背景，导出透明PNG，可选择精细边缘处理。

本仓库提供独立应用源码及部署脚本，模型版本固定在 `app.json`。源码仓库不包含模型权重；已保存的AutoDL镜像内包含权重、独立运行环境和开机配置。

## 使用已准备好的镜像

镜像：`autodl-u2net-20261111`（`image-16318c587c`），平台显示3.09GB。已通过从保存镜像创建全新实例的自动启动、模型完整性与真实HTTP推理验证，证据见 [IMAGE_VALIDATION.json](IMAGE_VALIDATION.json)。公开发布状态以平台为准。

创建并启动实例后，直接打开“自定义服务6006”，上传图片并下载透明PNG。源码位于 `/root/autodl-active`，模型位于 `/root/autodl-active/models`，无需重新安装或下载。镜像说明见 [IMAGE_README.md](IMAGE_README.md)。

实例内环境检查命令：

```bash
/root/autodl-active/.venv/bin/python /root/autodl-active/runtime/doctor.py --project /root/autodl-active --models --http
```

## 环境与空间

- Ubuntu 22.04，Python 3.11（也允许3.12），每个应用独立虚拟环境。
- 使用CPU ONNX，不依赖GPU。建议4GB内存起测。
- 模型约 0.176GB，模型和输出建议预留 1GB；Python/CUDA依赖另计。系统盘建议至少保留15GB安装余量；最终以 `df -h` 为准。
- 许可：Apache-2.0（U2Net）；MIT（rembg）。
- [上游项目](https://github.com/xuebinqin/U-2-Net)。本项目添加中文网页、固定模型下载、部署和检查脚本，上游算法归原作者。

## 独立包部署

以下用于从源码另行安装；已使用上述镜像的用户直接打开6006即可。命令在AutoDL的Linux终端执行，项目仓库为 `zw2029181901/autodl-u2net`。

```bash
cd /root
git clone https://github.com/zw2029181901/autodl-u2net.git
cd /root/autodl-u2net
bash install.sh
# 可在无卡模式完成依赖安装和模型下载；GPU应用实际推理须有卡模式。
.venv/bin/python runtime/prefetch.py --project .
.venv/bin/python runtime/doctor.py --project . --models
bash start.sh
```

若Python不是3.11/3.12，先选择合适的基础镜像，或用 `PYTHON_BIN=/你的Python路径 bash install.sh`。
若PyPI下载慢，可显式使用清华源：`PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple bash install.sh`；PyTorch使用官方独立源。
若Hugging Face不可访问，可自行选择镜像端点：`HF_ENDPOINT=https://hf-mirror.com .venv/bin/python runtime/prefetch.py --project .`。这是下载源选项，不保证可达；仓库及revision不变。

打开实例的自定义服务6006。保持前台启动终端运行，或按 UPLOAD_GUIDE.md 的后台启动方式运行。网页出现后必须完成 SMOKE_TEST.md 的真实任务。
如需密码：`APP_USERNAME=user APP_PASSWORD='自行设置' bash start.sh`。公开镜像保存前不要把自己的密码写进代码或脚本。

## 模型和保存镜像

源码安装时，模型优先放入 `MODEL_ROOT` 指定目录或项目内已有的 `models` 目录，否则使用 `/root/autodl-tmp/autodl-models`。保存镜像只保存系统盘，数据盘模型不会随镜像分发。

本次已保存镜像将约176MB的U2Net模型打包在系统盘 `/root/autodl-active/models`，新实例无需再次下载。模型和输出建议预留空间见 MODEL_STORAGE.md；镜像计费容量以平台为准，每保存一份都应核对账号总额度。

## 验收与发布

看 SMOKE_TEST.md、PUBLICATION.md、IMAGE_README.md 和 IMAGE_VALIDATION.json。本次镜像已通过真实任务、新实例复建与开机启动测试；公开上架及审核以平台当前状态为准。
安装会保存 `installed-requirements.txt`，请在云端验收后保留它作为该镜像的依赖记录。没有自动更新依赖或模型的后台任务。
