# -*- coding:utf-8 -×-
import ConfigParser
'''
    利用ConfigParser进行配置文件的读写和修改保存等功能
'''
cfg =ConfigParser.ConfigParser()

# help(cfg.read)

cfg.read('imooc.ini')

cfg.set('userinfo','email','978364051@qq.com')

sections =cfg.sections()
for se in sections:
    print se
    print cfg.items(se)


cfg.write(open('imooc.ini','w')) #要使得修改生效必须把配置内容重新写回文件