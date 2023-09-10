import pymysql as sql
conn = sql.connect(
    host = 'localhost',
    user = 'root',
    password = '' ,
    database = '')

cur = conn.cursor()
cur.execute('create database hr_db')