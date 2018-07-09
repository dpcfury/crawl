# -*- coding:utf-8 -*-
import urlparse

from bs4 import BeautifulSoup
import re


class HtmlParser(object):
    def parser(self, page_url, html_cont):
        if html_cont is None:
            return

        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        next_url = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(soup)

        return next_url, new_data

    def _get_new_urls(self, page_url, soup):
        # <span class="next">
        #   <a href="https://movie.douban.com/subject/25827935/collections?start=20">后页&gt;</a>
        # </span>
        next_node = soup.find("a", class_="next")
        if next_node is not None:
            print "下一页链接:%s" % next_node["href"].encode("utf-8")
            return urlparse.urljoin(page_url, next_node['href'])
        else:
            return None

    def _get_new_data(self, soup):
        result = []
        comment_items = soup.find_all("div", class_="comment-item")

        i = 0
        for comment_item in comment_items:
            rating_node = comment_item.find("span", class_=re.compile(r"allstar"))
            content_node = comment_item.find("div", class_="comment").find("p")
            if rating_node is not None and content_node is not None:
                res = {}

                rating_data = rating_node['class'][0].encode("utf-8")
                # print type(content_node.string)
                comment_data = content_node.get_text().strip().encode("utf-8")

                res["rating"] = rating_data
                res["comment"] = comment_data.replace("\n", " ")
                # 增加近结果集中
                result.append(res)

        i += 1
        return result

# def _get_one_data(item):
#     pl_node = item.find("p", class_="pl")
#     rating_node = pl_node.find("span", class_=re.compile(r"allstar"))
#     if rating_node is not None:  # 即有评分的时候这条记录才需要采集
#         comment_node = pl_node.next_sibling.next_sibling  # 之所以是两次是因为第一次是一个 ,\n 这个必须解决
#         if comment_node is not None:
#             print "解析出的rating:%s , comment: %s " % (
#                 rating_node.get('class')[0].encode("utf-8"), comment_node.string.encode('utf-8'))
#             return rating_node.get('class')[0].encode("utf-8"), comment_node.string.encode('utf-8')
#
#     return None, None;
