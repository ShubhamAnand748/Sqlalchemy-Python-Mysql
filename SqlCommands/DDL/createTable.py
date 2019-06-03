import dbConnection.conn
db = dbConnection.conn

# DDL
result = db.engine.execute('CREATE TABLE l_person (person_id int NOT NULLAUTO_INCREMENT, person_first_name varchar(255) NOT NULL, person_last_name varchar(255), person_age int, PRIMARY KEY (person_id))')
try:
    print('tbl_person created: ', result)
except:
    print('tbl_person already exists or maybe some error while creating the tbl_person.')
