# U2Net 抠图

上传图片，一键去除背景，下载带透明通道的 PNG；支持精细边缘处理。

## 基本环境

- Ubuntu 22.04，Python 3.12
- 基础框架：PyTorch 2.8.0，CUDA 12.8
- 抠图引擎：rembg 2.0.67、ONNX Runtime 1.22.1，使用 CPU 推理

## 项目与模型

项目地址：https://github.com/zw2029181901/autodl-u2net

镜像内已包含源码、独立运行环境及 U2Net 模型，无需再次克隆、安装依赖或下载模型。

- 代码目录：`/root/autodl-active`
- Python：`/root/autodl-active/.venv/bin/python`
- 模型目录：`/root/autodl-active/models`
- 网页端口：`6006`

## 使用方法

1. 使用本镜像创建并启动实例。
2. 打开实例的“自定义服务 6006”。
3. 上传图片，点击“去除背景”，下载透明 PNG。

服务随实例启动。首次推理会初始化模型，耗时取决于实例 CPU 性能；精细边缘处理耗时更长。

## 环境验证代码

在实例终端执行以下命令，检查依赖、模型完整性及网页服务：

```bash
/root/autodl-active/.venv/bin/python /root/autodl-active/runtime/doctor.py --project /root/autodl-active --models --http
```

## 验收记录

已通过保存镜像后创建全新实例的验证：服务自动启动，模型校验通过，无需原实例数据盘，完成图片上传、实际抠图及透明 PNG 下载。实测主机包含 RTX 3090 与 RTX 3080 Ti；本应用实际使用 CPU 推理。

依赖及模型许可见项目内 `THIRD_PARTY.md` 与 `licenses`。
