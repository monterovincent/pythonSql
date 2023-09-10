import pymysql as sql_tr

sql_con = sql_tr.connect(
    user = 'root',
    password = '',
    host= 'localhost',
    database= 'hr_db'
)

cur = sql_con.cursor()
insert_query = '''
INSERT INTO dept_tbl(dept_name,dept_desc) 
VALUES(%s,%s)
'''
data_value = [
    ('Human Resource',   'product'),
    ('Accounting', 'Money'),
    ('Security',  'Protection' ),
    ]
cur.executemany(insert_query, data_value)
sql_con.commit()