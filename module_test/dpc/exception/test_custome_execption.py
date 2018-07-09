# -*- coding:utf-8 -*-
from custom_exception import CustomError

try:
    raise CustomError("用户自定义的异常")
except Exception as c:
    print type(c)
    print c
    print id(c)
