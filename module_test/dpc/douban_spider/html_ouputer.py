# -*- coding:utf-8 -*-


class HtmlOutputer(object):
    def __init__(self):
        self.data = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.data = self.data + new_data

    def output_txt(self):
        f = open('comments.txt', 'a')
        for item in self.data:
            print item.get("rating")[-2:], item.get("comment")
            # print "评分: %s ,评论:%s" % (item.get("rating")[0].encode("utf-8"), item.get("comment").encode("utf-8"))
            comment = item.get("comment")
            f.write("%s::%s \n" % (item.get("rating")[-2:-1], comment))
        f.close()
        self.data = []
