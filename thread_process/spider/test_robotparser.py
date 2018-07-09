# -*- coding:utf-8 -*-
import robotparser

rp = robotparser.RobotFileParser()
rp.set_url('http://www.baidu.com/robots.txt')
rp.read()
url = 'http://www.baidu.com'
user_agent = 'BadCrawler'
print rp.can_fetch(user_agent, url)
user_agent = 'Googlebot'
print rp.can_fetch(user_agent, url)
