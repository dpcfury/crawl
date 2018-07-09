# -*- coding:utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1", port=3306, db="test", user="dpc", passwd="dpc1994spark", charset="utf8")
cursor = conn.cursor()

"""
执行cursor的各种方法
"""
sql = "select * from students"
cursor.execute(sql)

rs = cursor.fetchall()
for item in rs:
    print "userid:%s, name=%s" % item
    print item[0]  # 只是测试一下发现原来Tuple还是可以用[index] 来访问的

cursor.close()
conn.close()
