# ComfyUI Prompt Helper

[![GitHub release](https://img.shields.io/badge/version-1.3.0-blue.svg)](https://github.com/your-repo/ComfyUI-Prompt_Helper)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE)

一个专业的 ComfyUI 自定义节点套件，提供提示词工程工具，包括本地 GGUF 文本编码器支持和系统提示词提取功能。

A professional ComfyUI custom node suite providing prompt engineering tools, including local GGUF text encoder support and system prompt extraction.

## 📄 更新日志

本文档的详细更新记录已集中维护在 `doc/update.md`，可点击查看完整变更历史： [查看更新日志](doc/update.md)
（若在某些渲染环境中无法自动跳转，请在仓库根目录打开 `doc/update.md`）

## ✨ 功能特性

### 🤖 Qwen3 Engineer
- 🔄 本地运行 GGUF 文本编码器 (通过 `llama-cpp-python`)
- 📝 集成官方系统提示词，专注于正向约束、纹理细节和相机设置
- 🔗 输出增强的提示词字符串，可连接到工作流中的其他节点
- 📖 模型卡片: [Qwen3-4B-Z-Image-Engineer](https://huggingface.co/BennyDaBall/qwen3-4b-Z-Image-Engineer)

### 📄 System Prompt Extractor
- 🎯 提供详细的英文和中文系统提示词
- 🌍 支持中英文切换
- 🔧 可与其他 LLM 优化节点串联使用

## 🚀 安装指南

### 基本安装
1. **放置文件**: 将此仓库放置在 `ComfyUI/custom_nodes/ComfyUI-Prompt_Helper/`
2. **安装依赖**: `pip install -r requirements.txt`
3. **下载模型**: 下载 GGUF 模型文件并放置在 `ComfyUI/models/text_encoders/` 目录下

### Windows 优化安装
- 使用提供的本地 wheel 文件进行快速安装
- 支持 GPU 加速推理

## 📖 使用方法

### Qwen3 Engineer 节点
1. **重启 ComfyUI**: 节点类别为 `QwenTextEngineer`
2. **选择模型**: 自动扫描 `models/text_encoders` 目录中的 `.gguf` 文件
3. **配置参数**: 系统提示词已预填充，根据需要调整
4. **输入提示**: 在 `prompt` 字段中输入简短描述
5. **运行节点**: 输出丰富的正向提示词，可用于下游节点

### System Prompt Extractor 节点
1. **添加节点**: 从 `PromptHelper` 类别中添加 `System Prompt Extractor` 节点
2. **选择语言**: 选择 `English` 或 `Chinese`
3. **运行节点**: 获取对应的图像提示词改写系统提示词
4. **串联使用**: 将输出连接到其他 LLM 节点进行提示词优化

## 🔧 节点说明

| 节点名称 | 类别 | 功能描述 |
|---------|------|---------|
| QwenImageEngineer | QwenTextEngineer | 本地 GGUF 文本编码器，支持 Z-Image Turbo 提示词优化 |
| SystemPromptExtractor | PromptHelper | 系统提示词提取器，支持中英文切换 |

## 📄 更新日志

详细的更新日志请查看 [doc/update.md](doc/update.md)

## ⚙️ 参数配置

### Qwen3 Engineer 参数
- **gguf_name**: GGUF 模型文件名 (自动扫描)
- **system_prompt**: 系统提示词 (预填充)
- **prompt**: 用户输入的原始提示词
- **n_ctx**: 上下文长度 (默认 4096)
- **n_gpu_layers**: GPU 层数 (-1 表示全部加载到 GPU)
- **max_new_tokens**: 最大生成 token 数
- **temperature**: 采样温度 (0-1)
- **seed**: 随机种子 (-1 使用随机种子)

### System Prompt Extractor 参数
- **language**: 语言选择 (English/Chinese)

## 🔍 常见问题

### Qwen3 Engineer
**Q: llama-cpp-python 缺失怎么办？**
A: 重新安装依赖包然后重启 ComfyUI。

**Q: 找不到 GGUF 文件？**
A: 确保模型文件存在于 `models/text_encoders` 目录中。

**Q: 如何获得更好的生成效果？**
A: 适当调整 temperature 参数，建议在 0.7-0.9 之间。

### System Prompt Extractor
**Q: 如何使用提取的系统提示词？**
A: 将输出连接到其他支持系统提示词的 LLM 节点。

**Q: 支持哪些语言？**
A: 当前支持英文和中文两种语言的系统提示词。

## 📄 许可证

Apache-2.0 License - 遵循上游模型的许可证协议