# -*- coding:utf-8 -*-
f= open('import_test.py','r+')
print f.name
print f.mode
print f.readline()
f.writelines(['print "hello,world" ','print "haha"']) #这种R+方式会直接从文件头开始覆盖
print f.read()
f.close()

f2 =open("segwords.py",'w+')
f2.writelines(['print "hello,world" ','print "haha"']) # 我曹这种方式更狠 直接先删光再写 厉害
print f2.read()
f2.close()
