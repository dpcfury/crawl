# -*-coding:utf-8 -*-
import jieba
import test_re
file_input = open("comments_animal.txt", "r")
file_ouput = open("comments_animal_cut.txt", "w")

try:
    for line in file_input:
        print "读取内容:%s" % line
        temp = line.split("::")
        rating = temp[0]
        comments = temp[1]
        # 对评论做标点清洗
        # comments = test_re.filterMark(comments)
        words = "/".join(jieba.cut(comments, cut_all=False))
        file_ouput.write("%s::%s" % (rating.encode("utf8"), words.encode("utf8")))
except Exception as e:
    print "file error"
    print e
finally:
    file_ouput.close()
    file_input.close()
