# -*- coding:utf-8 -*-
import urllib2
import re

req = urllib2.urlopen("http://www.imooc.com/course/list")
buff = req.read()

imgurls = re.findall(r"http://.*.jpg", buff)
for item in imgurls:
    print item

i = 0
for url in imgurls:
    f = open(str(i) + ".jpg", "wb")
    req = urllib2.urlopen(url)
    buff = req.read()
    f.write(buff)
    i += 1
    # f.close()
