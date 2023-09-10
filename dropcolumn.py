import pymysql as sql_tr
from pymysql import err


sql_con = sql_tr.connect(
        user='root',
        password='',
        host='localhost',
        database='hr_db'
    )

cur = sql_con.cursor()
drop_col_tbl_sql = '''
                alter table emp_tbl
               drop column emp_gender
               '''
cur.execute(drop_col_tbl_sql)
cur.close()
