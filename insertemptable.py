import pymysql as sql_tr

sql_con = sql_tr.connect(
    user = 'root',
    password = '',
    host= 'localhost',
    database= 'hr_db'
)

cur = sql_con.cursor()
insert_query = '''
INSERT INTO person_tbl(per_name,per_email ,per_num) 
VALUES(%s,%s,%s)
'''
data_value = [
    ('John Bosco','dfhfffffgj@gmail.com', '3445555'),
    ('Ronald Roe','zxxert@gmail.com', '22232'),
    ('Jessical Joe','dsssdc@gmail.com','0987447'),
    ('Angel Gomez','rtoooyrhhtu@gmail.com','256896')
]
cur.executemany(insert_query, data_value)
sql_con.commit()