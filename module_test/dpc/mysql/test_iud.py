# -*- coding:utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1", port=3306, db="test", user="dpc", passwd="dpc1994spark", charset="utf8")
cursor = conn.cursor()

"""
执行cursor的各种方法
"""
sql_insert = "insert into students(name) values('程文华')"
sql_update = "update students set name='Russel' where userid =18"
sql_delete = "delete from students where userid <11"

try:
    cursor.execute(sql_insert)
    print cursor.rowcount  # 即使是提示过受影响的行数 并不代表数据库中内容产生了了实际的变化 需要进行事务的提交
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount

    # 提交事务才能对数据库产生真正的作用
    conn.commit()
except Exception as e:
    print e
    conn.rollback()

cursor.close()
conn.close()
