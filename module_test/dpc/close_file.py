# -*- coding:utf-8 -*-
import io
files =[]
for i in range(1099):
    files.append(open('imooc.txt','w'))
    print "%d : %d" % (i,files[i].fileno())#实际执行不能通过 不知道原因
