import dbConnection.conn
db = dbConnection.conn

# DCL

result = db.engine.execute("GRANT ALL ON tbl_person TO Anand")
try:
    print('One user granted with tbl_person table access: ', result)
except:
    print('Error')

