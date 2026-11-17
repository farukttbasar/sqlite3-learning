import sqlite3

# Connect to database
connect = sqlite3.connect('customers.db')

cursor = connect.cursor()

print("----------SEPERATOR-----------")

cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid LIMIT 2") 

items = cursor.fetchall()
for item in items:
    print(item)

print("----------SEPERATOR-----------")

cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2") 

items = cursor.fetchall()
for item in items:
    print(item)

print("----------SEPERATOR-----------")

cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid LIMIT 3") 

items = cursor.fetchall()
for item in items:
    print(item)

connect.commit()

connect.close()

