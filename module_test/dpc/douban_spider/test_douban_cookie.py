# -*- coding:utf-8 -*-
""" 登录之后拿到cookie 利用这个来查看下能不能拿到10页以后的短评


"""
import urllib2

req = urllib2.Request("https://movie.douban.com/subject/25827935/comments?start=280&limit=20&sort=new_score&status=P")
cookie = 'll="118163"; bid=b2br2LEVOC8; viewed="25867725"; gr_user_id=c1aa9d13-ae63-4196-8914-7d02dde27cf2; ct=y; ps=y; _ga=GA1.2.638048074.1475982684; ue="15606135595@163.com"; push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=AB944190D46BE858A1E4354DADD2F0C9|67dc3b7715c26611d2f864087fdcd71c; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1480941276%2C%22https%3A%2F%2Fwww.douban.com%2Faccounts%2Flogin%3Fsource%3Dmovie%22%5D; __utma=30149280.638048074.1475982684.1480938781.1480941276.34; __utmb=30149280.0.10.1480941276; __utmc=30149280; __utmz=30149280.1480908590.30.12.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; __utmv=30149280.15457; __utma=223695111.833287325.1475982684.1480938781.1480941276.29; __utmb=223695111.0.10.1480941276; __utmc=223695111; __utmz=223695111.1480908590.25.11.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; _pk_id.100001.4cf6=48590bdcb9ed43f7.1475982684.29.1480941718.1480938785.; _pk_ses.100001.4cf6=*; ap=1; dbcl2="154620411:2szaju8tQNY"'
req.add_header("Cookie", cookie)
req.add_header("User-Agent",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36")
req.add_header("Accept", "Atext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")

response = urllib2.urlopen(req)
if response.getcode() == 200:
    print response.read()
else:
    print response.info()
