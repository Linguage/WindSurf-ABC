import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    # 从环境变量获取密钥，如果不存在则使用默认值
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change-in-production'
    
    # 数据库配置 - 使用内存数据库进行测试
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
