# -*- coding:utf-8 -*-
class FileError(IOError):
    pass

try:
    raise FileError('File Error')  #也可以写成 raise FileError ,'描述信息' 打印的时候就会打印这个描述信息
except FileError as f:
    print f