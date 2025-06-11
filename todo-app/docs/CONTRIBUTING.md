# 贡献指南

感谢您有兴趣为待办事项应用做贡献！在提交您的贡献之前，请花点时间阅读以下指南。

## 开发环境设置

1. 克隆仓库：
   ```bash
   git clone <repository-url>
   cd todo-app
   ```

2. 创建并激活虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   .\venv\Scripts\activate  # Windows
   ```

3. 安装开发依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 设置环境变量：
   ```bash
   cp .env.example .env  # 复制示例环境变量文件
   # 编辑 .env 文件设置您的配置
   ```

5. 初始化数据库：
   ```bash
   python -c "from app import app, db; with app.app_context(): db.create_all()"
   ```

## 开发工作流

1. 从 `main` 分支创建一个新分支：
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. 进行更改并确保测试通过

3. 提交您的更改：
   ```bash
   git add .
   git commit -m "描述您的更改"
   ```

4. 推送到远程仓库：
   ```bash
   git push origin feature/your-feature-name
   ```

5. 创建一个 Pull Request

## 代码风格

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) Python 代码风格指南
- 使用 4 个空格作为缩进
- 使用双引号 (") 定义字符串
- 在操作符周围和逗号后添加空格
- 类和函数使用驼峰命名法 (CamelCase)
- 变量和函数名使用小写字母加下划线 (snake_case)

## 提交信息规范

请遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式调整（不影响代码运行的变动）
- `refactor`: 代码重构
- `test`: 测试用例
- `chore`: 构建过程或辅助工具的变动

示例：
```
feat: 添加用户认证功能
fix: 修复任务删除问题
docs: 更新 README 文件
```

## 报告问题

如果您发现任何错误或有功能建议，请通过 GitHub Issues 提交问题。在提交问题之前，请先搜索是否已有类似问题。

## 代码审查流程

1. 创建 Pull Request
2. 确保所有 CI 测试通过
3. 等待维护者审查代码
4. 根据反馈进行必要的更改
5. 代码被合并到主分支

## 行为准则

请确保您的行为符合我们的 [行为准则](CODE_OF_CONDUCT.md)。

## 许可证

通过提交贡献，您同意您的贡献将根据项目的 [MIT 许可证](LICENSE) 进行许可。
