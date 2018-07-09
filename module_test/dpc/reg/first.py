# -*- coding:utf-8 -*-
import re  # python正则表达式模块

str1 = "imooc python"
pa = re.compile(r"imooc")
print repr(type(pa))
ma = pa.match("imooc")
print repr(ma.re)
print ma.group()
print ma.span()
print ma.string

print re.match(r"imooc", 'imooc java', re.I).group()

print re.match(r"{.}", "{a}", re.I).group()

print re.match(r"{[a-zA-Z0-9]}", "{0}").group()

print re.match(r"{\w}", "{0}").group()

print re.match(r"\[[\w]\]", "[a]").group()  #pattern中存在[]要进行\转义
