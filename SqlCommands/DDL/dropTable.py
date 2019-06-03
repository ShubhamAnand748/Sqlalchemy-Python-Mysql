import dbConnection.conn
db = dbConnection.conn

# DDL
result = db.engine.execute('DROP TABLE tbl_person')
try:
    print('tbl_person deleted: ', result)
except:
    print('Error')

