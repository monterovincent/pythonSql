import pymysql as sql_tr
from pymysql import err


sql_con = sql_tr.connect(
        user='root',
        password='',
        host='localhost',
        database='hr_db'
    )

cur = sql_con.cursor()
cha_tbl  =   '''
                alter table emp_tbl
               rename to employee_tbl
               '''
cur.execute(cha_tbl)
