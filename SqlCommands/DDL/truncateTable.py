import dbConnection.conn
db = dbConnection.conn

# DDL
result = db.engine.execute('TRUNCATE TABLE tbl_person')
try:
    print('tbl_person data deleted: ', result)
except:
    print('Error')



