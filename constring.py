import pymysql as sql
conn = sql.connect(
    host = 'local host',
    user = 'root',
    password = '' ,
    database = ''

)

cur = conn.cursor()
cur.execute('select version() ')
ver= cuf.fetechone()
print(ver)