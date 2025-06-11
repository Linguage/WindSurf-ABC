#!/bin/bash

# 查找并显示 Flask 进程
echo "正在查找 Flask 服务器进程..."
pids=$(pgrep -f "flask run")

if [ -z "$pids" ]; then
    echo "没有找到正在运行的 Flask 服务器"
else
    echo "正在停止 Flask 服务器 (PID: $pids)..."
    kill $pids
    echo "Flask 服务器已停止"
fi
