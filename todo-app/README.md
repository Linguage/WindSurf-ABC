# 待办事项应用# Todo App

一个简单的待办事项应用，使用 Flask 和 SQLite 构建。

## 功能特点

- 创建、查看、更新和删除任务
- 标记任务完成状态
- 为任务设置截止日期
- 按状态筛选任务（全部、进行中、已完成）

## 项目结构

```
todo-app/
├── .env                    # 环境变量
├── .gitignore
├── README.md
├── requirements.txt        # 项目依赖
├── scripts/               # 脚本文件
│   ├── start.sh          # 启动脚本
│   └── stop.sh           # 停止脚本
├── src/                   # 源代码
│   ├── todo_app/         # Flask 应用
│   │   ├── __init__.py
│   │   ├── app.py        # 主应用文件
│   │   ├── config.py     # 配置文件
│   │   ├── static/       # 静态文件
│   │   └── templates/    # 模板文件
│   ├── init_db.py        # 数据库初始化脚本
│   └── run.py            # 运行脚本
└── tests/                # 测试文件
```

## 开始使用

### 前提条件

- Python 3.7+
- pip

### 安装步骤

1. 克隆仓库：
   ```bash
   git clone <repository-url>
   cd todo-app
   ```

2. 创建并激活虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 创建 `.env` 文件：
   ```bash
   cp .env.example .env
   ```
   
   然后编辑 `.env` 文件，设置你的配置。

### 运行应用

1. 启动服务：
   ```bash
   ./scripts/start.sh
   ```

2. 在浏览器中访问：
   ```
   http://127.0.0.1:5000
   ```

3. 停止服务：
   ```bash
   ./scripts/stop.sh
   ```

### 初始化数据库

如果需要重新初始化数据库：

```bash
python src/init_db.py
```

## 开发

### 运行测试

```bash
python -m pytest tests/
```

### 代码风格

项目使用 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 代码风格。

## 贡献指南

1. Fork 本仓库
2. 创建新分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。
