# -*- coding:utf-8 -*-
import os
f =os.open('imooc.txt',os.O_CREAT |os.O_RDWR)
line = os.read(f,2)
print line
os.close(f)

print os.access('./imooc.data',os.W_OK)

print os.listdir('/')

