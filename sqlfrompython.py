from multiprocessing.dummy import connection
from select import select

    
import pymysql
def connect_db():
    try:
        conn = pymysql.connect(user='root', password='root', host='localhost', database='test', port=3306, charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor, autocommit=True, connect_timeout=5, read_timeout=5, write_timeout=5)
        print('db connected')
        return conn
    except:
        print('db connection failed')
        return None
def disconnect_db():
    try:
        connection.close()
        print('db disconnected')
    except:
        print('db disconnection failed')

def create_table():
    try:
        with cursor() as cursor:
            sqlquery = "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))"
            cursor.execute(sqlquery)
            if count==0:
                print('table created')
            else:
                print('table already exists')
            cursir.close()
            disconnect_db()
            
    except:
        print('table creation failed')

create_table()
