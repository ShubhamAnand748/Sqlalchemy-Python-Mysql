import dbConnection.conn
db = dbConnection.conn

# DQL

#allUsers
result = db.engine.execute("SELECT * FROM tbl_person")

for data in result:
    print('ALL Users: ', data)

#conditionBasedUsers
result1 = db.engine.execute("SELECT * FROM tbl_person WHERE person_address = 'Chandigarh'")

for data1 in result1:
    print('Users from Chandigarh: ', data1)

#conditionBasedUsers
result2 = db.engine.execute("SELECT person_first_name, person_age FROM tbl_person WHERE person_address = 'Chandigarh'")

for data2 in result2:
    print('Users first name and age who is from Chandigarh: ', data2)

