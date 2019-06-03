import dbConnection.conn
db = dbConnection.conn

# DDL

"""
result = db.engine.execute('ALTER TABLE tbl_person ADD person_address varchar(255)')  # To add a new column in the table
try:
    print('One column added in tbl_person: ', result)
except:
    print('Error')
"""

result1 = db.engine.execute('ALTER TABLE tbl_person MODIFY COLUMN person_first_name varchar(255);')  # To modify existing column in the table
try:
    print('One column modify in tbl_person: ', result1)
except:
    print('Error')
