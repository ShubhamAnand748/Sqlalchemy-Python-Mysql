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
result = engine.execute('CREATE TABLE tbl_person (person_id int NOT NULL, person_first_name varchar(255) NOT NULL, person_last_name varchar(255), person_age int, PRIMARY KEY (person_id))')
try:
    print('tbl_person created: ', result)
except:
    print('tbl_person already exists or maybe some error while creating the tbl_person.')
