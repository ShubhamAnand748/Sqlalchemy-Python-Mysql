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

"""
result = engine.execute('ALTER TABLE tbl_person ADD person_address varchar(255)')  # To add a new column in the table
try:
    print('One column added in tbl_person: ', result)
except:
    print('Error')
"""

result1 = engine.execute('ALTER TABLE tbl_person MODIFY COLUMN person_first_name varchar(255);')  # To modify existing column in the table
try:
    print('One column modify in tbl_person: ', result1)
except:
    print('Error')
