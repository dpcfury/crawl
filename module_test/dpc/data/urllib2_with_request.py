# -*- coding:utf-8 -*-
import urllib2

request = urllib2.Request("http://www.baidu.com")

# 添加数据
request.add_data("cao")

# 添加http的header
request.add_header("User-Agent", "Mozilla/5.0")

response = urllib2.urlopen(request)

print response.getcode()
