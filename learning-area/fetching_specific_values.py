import sqlite3

# Connect to database
connect = sqlite3.connect('customers.db')

cursor = connect.cursor()

cursor.execute("SELECT rowid, * FROM customers WHERE last_name = 'Brown'")

"""
cursor.fetchone() LAST ITEM
cursor.fetchmany(number) FETCHES number ITEMS
cursor.fetchall()
"""

items = cursor.fetchall()
for item in items:
    print(item)
# you can get a better output usinh loops, \t, \n, etc.

print("----------------SEPERATOR----------------")

cursor.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%'")

items = cursor.fetchall()
for item in items:
    print(item)

# WHERE age <, >, >=, <=, =, LIKE, etc. ...

connect.commit()

connect.close()

