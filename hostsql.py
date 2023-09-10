import pymysql as sql_tr

sql_con = sql_tr.connect(
    user = 'root',
    password = '',
    host= 'localhost',
    database= 'nhappdb'
)

cur = sql_con.cursor()
drop_tbl_sql = 'drop table customer'
cur.execute(drop_tbl_sql)
cur.close()