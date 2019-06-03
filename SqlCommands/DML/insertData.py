import dbConnection.conn
db = dbConnection.conn

# DML

#insert one row
result = db.engine.execute("INSERT INTO tbl_person (person_first_name, person_last_name, person_age, person_address) VALUES ('Shubham', 'Anand', '22', 'Chandigarh')")
try:
    print('One row inserted: ', result)
except:
    print('Error')


#insert multiple rows
result1 = db.engine.execute("INSERT INTO tbl_person (person_first_name, person_last_name, person_age, person_address) VALUES ('Anand', 'Shubham', '22', 'Chandigarh'), ('Shubham', '', '22', 'Chandigarh'), ('Anand', '', '22', 'Chandigarh')")
try:
    print('One or more row inserted: ', result1)
except:
    print('Error')

