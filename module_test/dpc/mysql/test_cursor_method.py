# -*- coding:utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1", port=3306, db="test", user="dpc", passwd="dpc1994spark", charset="utf8")
cursor = conn.cursor()

"""
执行cursor的各种方法
"""
sql = "select * from students"
cursor.execute(sql)
print cursor.rowcount

rs = cursor.fetchone()
print rs

rs = cursor.fetchmany(3)
print rs

rs = cursor.fetchall()
print rs
cursor.close()
conn.close()
