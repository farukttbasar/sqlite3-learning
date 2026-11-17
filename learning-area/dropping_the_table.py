import sqlite3

# Connect to database
connect = sqlite3.connect('customers.db')

cursor = connect.cursor()

"""
cursor.execute("DROP TABLE costumers")
connect.commit()

THESE TWO LINES DELETES ALL THE TABLE AND IT IS PERMANENT !
"""

cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()

cursor.fetchall()
for item in items:
    print(item)

connect.commit()

connect.close()

