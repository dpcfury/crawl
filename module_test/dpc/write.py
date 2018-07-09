# -*- coding:utf-8 -*-
f =open('imooc.txt','w')
for i in range(100):
    f.write('test :'+str(i)+'\n') # 写文件要注意缓存区大小的问题 通过close和flush会主动吧缓存区内容写入Disk

f.close()