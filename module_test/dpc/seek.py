# -*- coding:utf-8 -*-
import os
f=open('imooc.txt','r+')
f.read(2)
f.seek(-1,os.SEEK_CUR)
print f.read(2)
print f.tell()