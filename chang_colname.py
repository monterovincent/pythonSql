import pymysql as sql_tr
from pymysql import err


sql_con = sql_tr.connect(
        user='root',
        password='',
        host='localhost',
        database='hr_db'
    )

cur = sql_con.cursor()
change_col = '''
            alter table emp_tbl
           change column emp_pos emp_posit
           varchar(50) not null
           after emp_age
'''
cur.execute(change_col)