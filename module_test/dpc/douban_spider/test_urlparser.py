# -*- coding:utf-8 -*-
import urlparse

if __name__ == "__main__":
    page_url = "https://movie.douban.com/subject/25827935/comments"
    new_url = "?start=22&limit=20&sort=new_score&status=P"
    new_full_url = urlparse.urljoin(page_url, new_url)
    print "拼接好的新的url: %s" % new_full_url