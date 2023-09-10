import pymysql as sql_tr
from pymysql import err


sql_con = sql_tr.connect(
        user='root',
        password='',
        host='localhost',
        database='hr_db'
    )

try:
    alt_col = '''
    alter table emp_tbl
    add emp_gender varchar(15)
    after emp_age,
    add emp_pos varchar(50) not null
    after emp_salary
    '''
    cur = sql_con.cursor()
    cur.execute(alt_col)

except sql_tr.err.OperationalError:
    print('unable to alter table')
except sql_tr.err.ProgrammingError:
    sql_con.rollback()
    print('unable to alter table, check query')
finally:
   print('table altered successfully')
cur.close()
