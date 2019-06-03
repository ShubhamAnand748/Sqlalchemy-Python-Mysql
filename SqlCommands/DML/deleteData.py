import dbConnection.conn
db = dbConnection.conn

# DML

result = db.engine.execute("DELETE FROM tbl_person WHERE person_id = 4")
try:
    print('One row deleted: ', result)
except:
    print('Error')

