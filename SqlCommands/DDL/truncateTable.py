from sqlalchemy import create_engine

#mysql+mysqldb://<user>:<password>@<host>[:/port]/<dbname>
#mysql+pymysql://<user>:<password>@<host>[:/port]/<dbname>

db_url = 'mysql+pymysql://root:emilence@localhost:3306/chat-app'
engine = create_engine(db_url)
conn = engine.connect()

try:
    print('Connection has been established successfully.\nHere you can perform DDL operation.\nConnection object is: {}'.format(conn))
except:
    print('Unable to connect to the database.')

# DDL
result = engine.execute('TRUNCATE TABLE tbl_person')
try:
    print('tbl_person data deleted: ', result)
except:
    print('Error')



