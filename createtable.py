import pymysql as sql
conn = sql.connect(
     host= 'localhost',
    user= 'root',
    password = '',
    database = 'hr_db')

cur = conn.cursor()
cv_tbl = '''create table emp_tbl(
               id int primary key auto_increment,
               emp_name varchar(50) not null,
               emp_age int,
               emp_dob date not null,
               emp_salary decimal(10,2)) '''
cur.execute(cv_tbl)
