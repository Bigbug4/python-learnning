#!/usr/bin/env python3
# coding=utf-8

import pymysql
conn = pymysql.connect(host="localhost",user="root",passwd="dcl0501",db="mysite1",port=3306,charset="utf8")
cur = conn.cursor()
# cur.execute("insert into users (username,password,email) values (%s,%s,%s)",("perl","14456276","perl@gmail.com"))
# conn.commit()
a = cur.execute("select * from user")
print(a)
lines = cur.fetchall()
for line in lines:
    print(line)

cur.close()
conn.close()