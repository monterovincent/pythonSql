import pymysql as sql_tr
from pymysql import err


sql_con = sql_tr.connect(
        user='root',
        password='',
        host='localhost',
        database='acct_db'
    )

try:

    cur = sql_con.cursor()
    tbl_cr = '''
        create table user_tbl(
        id int primary key auto_increment,
        name varchar(100) not null,
        gender varchar(20),
        dob date not null,
        height decimal(3,1) 
        )
    '''
    cur.execute(tbl_cr)

except sql_tr.err.OperationalError:
    print('Unable to create table, it is already in existence')

except sql_tr.err.ProgrammingError:
    sql_con.rollback()
    print('Unable to create Table check your query')

finally:
    print('Table created successfully')
cur.close()