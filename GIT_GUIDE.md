# Git 配置指南

本文档说明了 Windsurf 编程教程项目的 Git 配置和最佳实践。

## 基础配置

### 1. 用户信息配置

```bash
# 配置用户名和邮箱（全局配置）
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 或者为当前项目单独配置
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### 2. 默认分支配置

```bash
# 设置默认分支为 main
git config --global init.defaultBranch main
```

### 3. 编辑器配置

```bash
# 设置默认编辑器（可选）
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "vim"          # Vim
```

## 项目特定配置

### 分支策略

本项目推荐使用以下分支策略：

- `main` - 主分支，稳定版本
- `develop` - 开发分支，集成功能
- `feature/*` - 功能分支，开发新功能
- `hotfix/*` - 热修复分支，紧急修复

### 提交信息规范

遵循 Conventional Commits 规范：

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**类型 (type)：**
- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式化（不影响功能）
- `refactor`: 代码重构
- `test`: 添加或修改测试
- `chore`: 维护性工作

**示例：**
```bash
git commit -m "feat: 添加温度数据可视化功能"
git commit -m "docs: 更新 README 安装说明"
git commit -m "fix: 修复待办事项删除功能"
```

### 忽略文件规则

`.gitignore` 文件已配置以下忽略规则：

- 操作系统文件（.DS_Store, Thumbs.db）
- 编辑器配置文件（.vscode/, .idea/）
- Python 编译文件（__pycache__/, *.pyc）
- 环境配置（.env, venv/）
- 数据库文件（*.db, *.sqlite）
- 日志文件（*.log）
- 临时文件（*.tmp, *.bak）

## 常用 Git 命令

### 基础操作

```bash
# 查看状态
git status

# 添加文件
git add .                    # 添加所有文件
git add filename             # 添加特定文件

# 提交更改
git commit -m "提交信息"

# 查看历史
git log --oneline            # 简洁格式
git log --graph              # 图形化显示
```

### 分支操作

```bash
# 创建并切换分支
git checkout -b feature/new-feature

# 切换分支
git checkout main

# 合并分支
git merge feature/new-feature

# 删除分支
git branch -d feature/new-feature
```

### 远程操作

```bash
# 添加远程仓库
git remote add origin https://github.com/username/windsurf-tutorial.git

# 推送到远程
git push -u origin main

# 拉取更新
git pull origin main
```

## 最佳实践

### 1. 提交频率

- 小步提交，频繁提交
- 每个提交只解决一个问题
- 确保每次提交都能编译和运行

### 2. 分支管理

- 从 main 分支创建功能分支
- 功能完成后通过 Pull Request 合并
- 定期更新功能分支与主分支同步

### 3. 代码审查

- 所有代码更改通过 Pull Request
- 至少一人审查后合并
- 确保测试通过后合并

### 4. 标签管理

```bash
# 创建版本标签
git tag -a v1.0.0 -m "版本 1.0.0"

# 推送标签
git push origin v1.0.0
```

## 协作指南

### Fork 工作流

1. Fork 项目到个人账户
2. Clone 到本地开发
3. 创建功能分支开发
4. 推送到个人 Fork
5. 创建 Pull Request

### 同步上游更新

```bash
# 添加上游仓库
git remote add upstream https://github.com/original/windsurf-tutorial.git

# 获取上游更新
git fetch upstream

# 合并到本地主分支
git checkout main
git merge upstream/main
```

## 问题排查

### 常见问题

1. **提交信息乱码**
   ```bash
   git config --global core.quotePath false
   ```

2. **行尾符号问题**
   ```bash
   git config --global core.autocrlf input  # macOS/Linux
   git config --global core.autocrlf true   # Windows
   ```

3. **撤销提交**
   ```bash
   git reset --soft HEAD~1    # 撤销最后一次提交，保留更改
   git reset --hard HEAD~1    # 撤销最后一次提交，丢弃更改
   ```

## 参考资源

- [Git 官方文档](https://git-scm.com/doc)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
