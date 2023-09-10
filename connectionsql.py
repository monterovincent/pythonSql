import pymysql as sql_tr
from pymysql import err

sql_con = sql_tr.connect(
    user='root',
    password='',
    host='localhost',
    database='hr_db'
)

try:

    cur = sql_con.cursor()
    sql_user = '''
       create table person_tbl(
       per_id int primary key auto_increment,
       per_name varchar(35) not null,
       per_email varchar(50) not null unique,
      per_num varchar(50) not null unique,
      per_country varchar(50) not null default 'Nigeria' 


       )
    '''
    cur.execute(sql_user)

except sql_tr.err.OperationalError:
    print('Unable to create Table')
except sql_tr.err.ProgrammingError:
    sql_con.rollback()
    print('Unable to create table, it is already in existence')
finally:
    print('Table created successfully')
cur.close()