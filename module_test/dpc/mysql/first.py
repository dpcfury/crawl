import MySQLdb

print MySQLdb
conn = MySQLdb.connect(host="127.0.0.1", port=3306, db="test", user="dpc", passwd="dpc1994spark", charset="utf8")
cursor = conn.cursor()

print conn
print cursor

cursor.close()
conn.close()

help(conn.cursor)
help(cursor)
