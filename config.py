#encoding:utf-8
import os
from datetime import timedelta

DEBUG = False

# 24字符的随机字符串作为SECRET_KEY
SECRET_KEY=os.urandom(24)
# 三天过期
PERMANENT_SESSION_LIFETIME = timedelta(days=3)


# 数据库配置
mysql_config={
    'host':'localhost',
    'port':3306,
    'user':'root',
    'password':'meimima123',
    'db':'flask',
    'charset':'utf8mb4',
}
