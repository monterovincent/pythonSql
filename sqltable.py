import pymysql as sql
conn = sql.connect(
    host = 'localhost',
    user = 'root',
    password = '' ,
    database = 'nhs_db')

cur = conn.cursor()

cur = sql_conn.cursor()
sql_user = '''
           create table user_tbl(
           user
           
           '''

