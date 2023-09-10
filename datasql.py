import pymysql as sql_tr
import pymysql
sql_con = sql_tr.connect(
        user='root',
        password='',
        host='localhost',
        database=''
    )

try:

    cur = sql_con.cursor()
    cur.execute('create database hr_db')



except sql_tr.err.OperationalError:
    print('Unable to connect')
except pymysql.err.ProgrammingError:
    sql_con.rollback()
    print('Check your query')
finally:
    print('print database created successfull!!')
cur.close()