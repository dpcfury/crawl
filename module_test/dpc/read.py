# -*- coding: utf-8 -*-
import io

f =open('file.py','r')
# L= f.readlines()
# for item in L:
#     print item
#
# f.close()
lines =0
iter = iter(f)
for line in iter:
    lines +=1
print lines

f.close()

