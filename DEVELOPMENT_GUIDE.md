# DeepSeek-V3 项目开发指南

## 项目结构

本项目采用 Git Submodule 的方式管理教程内容，主要包含两个仓库：
- 主仓库：DeepSeek-V3（当前仓库）
- 子模块：Tutorial（教程内容）

```
DeepSeek-V3/
├── README.md
├── training/
├── inference/
└── Tutorial/  # 作为子模块引入
```

## 分支策略

### Tutorial 仓库分支
- `camp4`: 原始教程内容分支，保持独立性
- `camp4_deepseek`: 专门用于 DeepSeek-V3 项目的定制分支

### DeepSeek-V3 仓库分支
- `main`: 主分支
- `doc`: 文档开发分支
- 其他功能分支根据需要创建

## 开发工作流程

### 1. 克隆项目
```bash
# 克隆主仓库和子模块
git clone --recurse-submodules git@github.com:1587causalai/DeepSeek-V3.git

# 如果已经克隆但没有子模块，执行：
git submodule update --init --recursive
```

### 2. Tutorial 内容开发
```bash
# 进入 Tutorial 目录
cd Tutorial

# 确保在正确的分支上
git checkout camp4_deepseek

# 进行修改并提交
git add .
git commit -m "your changes"
git push origin camp4_deepseek
```

### 3. 更新 Tutorial 内容
```bash
# 从 camp4 分支同步更新
cd Tutorial
git checkout camp4_deepseek
git merge camp4
git push origin camp4_deepseek

# 在主仓库中更新子模块引用
cd ..
git add Tutorial
git commit -m "update Tutorial submodule"
git push
```

### 4. DeepSeek-V3 主项目开发
```bash
# 确保在主仓库根目录
cd /path/to/DeepSeek-V3

# 创建新的功能分支
git checkout -b feature/your-feature

# 开发完成后提交
git add .
git commit -m "add new feature"
git push origin feature/your-feature
```

## 常用子模块操作

### 切换子模块分支
```bash
# 在主仓库中
git submodule set-branch -b new-branch Tutorial
git commit -am "switch Tutorial branch"
git push
```

### 更新子模块到最新版本
```bash
git submodule update --remote Tutorial
git commit -am "update Tutorial to latest version"
git push
```

### 查看子模块状态
```bash
git submodule status
```

## 注意事项

1. **保持分支独立性**
   - 不要在 `camp4` 分支上直接修改
   - 所有与 DeepSeek-V3 相关的修改都在 `camp4_deepseek` 分支上进行

2. **子模块更新**
   - 主仓库的提交需要同时包含子模块的更新
   - 确保子模块的更改已经推送到远程仓库

3. **冲突处理**
   - 如果从 `camp4` 合并到 `camp4_deepseek` 时发生冲突
   - 优先保持 DeepSeek-V3 相关的修改
   - 必要时创建新的文件而不是修改原有文件

4. **文档同步**
   - 确保文档更新与代码更改同步
   - 重要更改需要在两个仓库的文档中都有说明

## 最佳实践

1. **定期同步**
   - 定期从 `camp4` 分支同步更新到 `camp4_deepseek`
   - 保持与主项目的文档风格一致

2. **清晰的提交信息**
   - 提交信息要清晰说明更改内容
   - 重要更改要添加详细的说明

3. **独立的功能分支**
   - 新功能开发使用独立的分支
   - 完成后通过 Pull Request 合并

4. **及时的文档更新**
   - 代码更改的同时更新相关文档
   - 保持文档的实时性和准确性 