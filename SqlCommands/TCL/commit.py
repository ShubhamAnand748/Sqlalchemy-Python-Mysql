import dbConnection.conn
db = dbConnection.conn

# DCL

result = db.engine.execute("DELETE FROM tbl_person WHERE person_id = 5")
result1 = db.engine.execute("COMMIT")
try:
    print('Commit successfully: ', result1)
except:
    print('Error')


