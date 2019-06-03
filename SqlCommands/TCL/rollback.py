import dbConnection.conn
db = dbConnection.conn

# DCL

result = db.engine.execute("DELETE FROM tbl_person WHERE person_id = 6")
result1 = db.engine.execute("ROLLBACK")
try:
    print('Rollback successfully: ', result1)
except:
    print('Error')


