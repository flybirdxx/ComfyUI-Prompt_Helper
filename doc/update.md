# 更新日志 / Update Log

## [1.3.0] - 2024-12-31

### ✨ 新增功能 / New Features
- **SystemPromptExtractor 节点**: 新增系统提示词提取器节点
  - 内置详细的英文和中文系统提示词
  - 支持语言切换功能
  - 可以与其他 LLM 优化节点串联使用
- **PromptHelper 节点分类**: 新增节点分类用于组织提示词相关工具

### 📚 文档更新 / Documentation
- **README 重构**: 完全重写 README.md 文件
  - 添加中英文双语说明
  - 使用 emoji 提升视觉效果
  - 增加详细的目录结构
  - 提供更清晰的使用指南
- **新增更新日志**: 创建独立的更新日志文档 `doc/update.md`

### 🛠️ 技术改进 / Technical Improvements
- **代码结构优化**: 改善节点代码结构和注释
- **兼容性增强**: 确保新节点与现有 ComfyUI 环境的兼容性

## [1.2.0] - 2024-12-17

### ✨ 新增功能 / New Features
- **随机种子支持**: 新增 `seed` 参数，支持可复现的输出结果
  - 设置为 -1 时使用随机种子
  - 设置为具体数值时保证输出一致性

### 🐛 修复 / Bug Fixes
- 优化参数验证逻辑
- 改进错误处理机制

## [1.1.0] - 2024-12-17

### 📦 构建优化 / Build Improvements
- **预编译文件更新**: 更新 wheel 文件到最新版本
- **Windows 安装优化**: 提供本地 wheel 文件支持快速安装

### 🛠️ 开发工具 / Development Tools
- **新增 .gitignore**: 添加版本控制忽略文件
  - 忽略 Python 缓存目录 `__pycache__`
  - 忽略临时文件和日志文件

### 📚 文档更新 / Documentation
- 优化安装指南
- 添加 Windows 用户特殊说明

## [1.0.0] - 2024-12-17

### 🚀 初始发布 / Initial Release

#### ✨ 核心功能 / Core Features
- **Qwen3 Engineer 节点**: 专业的提示词工程节点
  - 本地 GGUF 文本编码器支持
  - 集成 Z-Image Turbo 专用系统提示词
  - 自动扫描 `models/text_encoders` 目录
  - 支持正向约束和纹理细节优化

#### 🛠️ 技术特性 / Technical Features
- **llama-cpp-python 集成**: 通过 llama-cpp-python 实现本地推理
- **GPU 加速支持**: 支持 GPU 层加载优化性能
- **参数化配置**: 完整的参数控制
  - 上下文长度配置 (`n_ctx`)
  - GPU 层数设置 (`n_gpu_layers`)
  - 生成长度限制 (`max_new_tokens`)
  - 温度采样控制 (`temperature`)

#### 📦 安装与部署 / Installation & Deployment
- 标准 ComfyUI 自定义节点安装流程
- 自动依赖管理
- 模型文件自动扫描

#### 📚 文档 / Documentation
- 完整的安装指南
- 详细的使用说明
- 参数配置说明
- 常见问题解答

---

## 📋 更新说明 / Update Notes

### 版本命名规则 / Version Naming Convention
- **主要版本** (Major): 不兼容的 API 变更
- **次要版本** (Minor): 向后兼容的新功能
- **补丁版本** (Patch): 向后兼容的错误修复

### 兼容性保证 / Compatibility Guarantee
- 次要版本和补丁版本保证向后兼容
- 主要版本可能包含破坏性变更

### 获取最新版本 / Getting Latest Version
```bash
# 通过 git 更新
git pull origin main

# 或重新下载最新版本
```

---

## 🤝 贡献 / Contributing

欢迎提交问题报告和功能请求！

Please submit issues and feature requests!

## 📞 联系方式 / Contact

- 项目主页: [GitHub Repository]
- 问题反馈: [Issues]
- 讨论交流: [Discussions]
