# -*- coding:utf-8 -*-
from  bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 根据html网页字符串创建BeautifulSoup对象
soup = BeautifulSoup(
    html_doc, # html文档字符串
    "html.parser", # html解析器
    from_encoding="utf-8" # html文档的编码
)

# 方法 fina_all(name, attr ,string)

# 查找所有便签为a的节点
links = soup.find_all("a")
for link in links:
    print "名称", link.name, link["href"], link.get_text()

print "获取lacie的这个url的链接"
soup_node = soup.find("a", href="http://example.com/lacie")
print soup_node.name, soup_node["href"], soup_node.get_text()

print "正则匹配"
soup_node = soup.find("a", href=re.compile(r"illi"))
print soup_node.name, soup_node["href"], soup_node.get_text()

print "class匹配"
link_node = soup.find("p", class_="title")
print link_node.name, link_node['class'], link_node.get_text()

