from sqlalchemy import create_engine

#mysql+mysqldb://<user>:<password>@<host>[:/port]/<dbname>
#mysql+pymysql://<user>:<password>@<host>[:/port]/<dbname>

db_url = 'mysql+pymysql://root:emilence@localhost:3306/chat-app'
engine = create_engine(db_url)
conn = engine.connect()

try:
    print('Connection has been established successfully. \nConnection object is: {}'.format(conn))
except:
    print('Unable to connect to the database.')

result = engine.execute('SELECT * FROM tbl_user')
for data in result:
    print('UserData: ', data)

#insertData = engine.execute("INSERT INTO tbl_user (user_first_name, user_email, user_password) VALUES ('ShubhamAnand', 'a@exp.com', '')")
#print('One Row inserted: ', insertData)


updateData = engine.execute("UPDATE tbl_user SET user_first_name='Shubham' WHERE user_id='11'")
print('One Row updated: ', updateData)

allUsers = engine.execute('SELECT * FROM tbl_user')
for data1 in allUsers:
    print('UserData: ', data1)