import pymysql as sql_tr
from pymysql import err


sql_con = sql_tr.connect(
        user='root',
        password='',
        host='localhost',
        database='hr_db'
    )

cur = sql_con.cursor()
trunc_tbl = '''
               truncate table person_tbl 
               
               '''
cur.execute(trunc_tbl)
