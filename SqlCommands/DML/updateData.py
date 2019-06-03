import dbConnection.conn
db = dbConnection.conn

# DML

result = db.engine.execute("UPDATE tbl_person SET person_last_name ='Anand', person_address ='Mohali' WHERE person_id = 3")
try:
    print('One row updated: ', result)
except:
    print('Error')

