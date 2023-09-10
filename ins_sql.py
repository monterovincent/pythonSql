import pymysql as sql
conn = sql.connect(
      host = 'localhost',
      user = 'root',
      password = "",
      database = 'hr_db')

cur = conn.cursor()
ins_dt = '''insert into emp_tbl(emp_name, emp_age,emp_dob,emp_salary)
               values('paul',36,'1987-3-5', 265537.10)

           '''
cur.execute(ins_dt)
conn.commit()

