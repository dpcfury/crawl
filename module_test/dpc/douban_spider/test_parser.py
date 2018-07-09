# -*- coding:utf-8 -*-
import urllib2

import re
from bs4 import BeautifulSoup

start_url = "https://movie.douban.com/subject/25827935/comments"
response = urllib2.urlopen(start_url)
if response.getcode() == 200:
    http_cont = response.read()
    soup = BeautifulSoup(http_cont, "html.parser", from_encoding="utf-8")
    soup.prettify()
    next_node = soup.find("a", class_="next")
    if next_node is not None:
        print "下一页链接为:%s" % next_node['href'].encode("utf-8")
    else:
        print "没有下一页"

    comment_items = soup.find_all("div", class_="comment-item")
    i = 1
    for comment_item in comment_items:
        rating_node  = comment_item.find("span",class_=re.compile(r"allstar"))
        content_node  = comment_item.find("div",class_="comment").find("p")
        if rating_node is not None:
            print "评分为: %s " % rating_node['class'][0].encode("utf-8")
        if content_node is not None:
            print "评论内容为: %s " % content_node.get_text().encode("utf-8")
        i += 1


else:
    print "请求失败: %d" % response.getcode()
