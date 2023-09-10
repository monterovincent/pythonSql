import pymysql as sql_tr
from pymysql import err

sql_con = sql_tr.connect(
        user='root',
        password='',
        host='localhost',
        database=''
    )

try:

    cur = sql_con.cursor()
    cur.execute('select version()')
    sql_ver = cur.fetchone()
    print(sql_ver)

except sql_tr.err.OperationalError:
    print('Unable to connect')
except sql_tr.err.ProgrammingError:
    sql_con.rollback()
    print('Connetion Failed')
finally:
    print('Connet Successfully!!')
cur.close()