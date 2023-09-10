import pymysql as sql_tr

sql_con = sql_tr.connect(
    user = 'root',
    password = '',
    host= 'localhost',
    database= 'hr_db'
)

cur = sql_con.cursor()
insert_query = '''
INSERT INTO emp_tbl(emp_name,emp_age ,emp_dob, emp_salary) 
VALUES(%s,%s,%s,%s)
'''
data_value = [
    ('John Bosco',23,'1999-03-23', 34567.89),
    ('Ronald Roe',44 ,'1934-09-21', 93564),
    ('Jessical Joe',34,'2004-02-15',34444),
    ('Angel Gomez',22,'2021-07-11',372321)
]
cur.executemany(insert_query, data_value)
sql_con.commit()