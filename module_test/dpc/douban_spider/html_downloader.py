# -*- coding:utf-8 -*-
import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        req = urllib2.Request(url)
        cookie = 'll="118163"; bid=b2br2LEVOC8; viewed="25867725"; gr_user_id=c1aa9d13-ae63-4196-8914-7d02dde27cf2; ct=y; ps=y; _ga=GA1.2.638048074.1475982684; ue="15606135595@163.com"; dbcl2="154620411:2szaju8tQNY"; ck=PGxO; ap=1; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1480990822%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=AB944190D46BE858A1E4354DADD2F0C9|67dc3b7715c26611d2f864087fdcd71c; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=48590bdcb9ed43f7.1475982684.31.1480990838.1480947793.; _pk_ses.100001.4cf6=*; __utma=30149280.638048074.1475982684.1480947753.1480990420.36; __utmb=30149280.4.10.1480990420; __utmc=30149280; __utmz=30149280.1480908590.30.12.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; __utmv=30149280.15462; __utma=223695111.833287325.1475982684.1480947753.1480990822.31; __utmb=223695111.0.10.1480990822; __utmc=223695111; __utmz=223695111.1480990822.31.12.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/'
        req.add_header("Cookie", cookie)
        req.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36")
        req.add_header("Accept", "Atext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        req.add_header("Host", "movie.douban.com")
        response = urllib2.urlopen(req)
        # response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
