# -*- coding:utf-8 -*-
try:
    raise TypeError('错误')  # 也可以写成raise TypeError ,"错误"
except TypeError as e:
    print e

assert 1 == 1, '不是吗难道'


