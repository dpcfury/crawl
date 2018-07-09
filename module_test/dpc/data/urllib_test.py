# -*- coding :utf-8 -*-
import urllib2

response = urllib2.urlopen("http://www.baidu.com")

# 判断返回的状态吗 如果是200 表示获取成功
print response.getcode()

# 读取内容
print response.read()
