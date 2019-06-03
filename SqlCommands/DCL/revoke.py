import dbConnection.conn
db = dbConnection.conn

# DCL

result = db.engine.execute("REVOKE UPDATE ON tbl_person FROM ANAND")
try:
    print('Permission revoked: ', result)
except:
    print('Error')

