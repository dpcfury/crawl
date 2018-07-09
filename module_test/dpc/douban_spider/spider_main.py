# -*- coding:utf-8 -*-
import time

from dpc.douban_spider import html_downloader
from dpc.douban_spider import html_ouputer
from dpc.douban_spider import html_parser
from dpc.douban_spider import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_ouputer.HtmlOutputer()

    def craw(self, url):
        count = 1
        self.urls.add_new_url(url)
        # try:
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print "正抓取第 %d 个页面: %s ...." % (count, new_url.encode("utf-8"))
            html_cont = self.downloader.download(new_url)
            next_url, new_data = self.parser.parser(new_url, html_cont)
            self.outputer.collect_data(new_data)
            if next_url is None:
                break
            else:
                self.urls.add_new_url(next_url)
            count += 1

            # 抓取2个页面休眠一次
            if count % 2 == 0:
                time.sleep(2)
            if count % 100 == 0:
                # 写如文件一次
                self.outputer.output_txt()
                time.sleep(10)

        self.outputer.output_txt()


if __name__ == "__main__":
    root_url = "https://movie.douban.com/subject/25827935/comments"  # 七月与安生
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
