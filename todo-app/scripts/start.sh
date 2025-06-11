#!/bin/bash

# 激活虚拟环境
source venv/bin/activate

# 设置环境变量
export FLASK_APP=src.todo_app.app
export FLASK_DEBUG=1
export FLASK_ENV=development

# 设置 Python 路径
export PYTHONPATH=$PWD/src:$PYTHONPATH

# 创建必要的目录
mkdir -p instance

# 检查5000端口是否被占用
if lsof -i :5000 > /dev/null; then
    echo "端口 5000 被占用，将在 5001 端口启动..."
    flask run --port=5001
else
    flask run
fi
