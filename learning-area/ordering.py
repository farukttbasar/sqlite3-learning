import sqlite3

# Connect to database
connect = sqlite3.connect('customers.db')

cursor = connect.cursor()

cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()
for item in items:
    print(item)

print("----------SEPERATOR-----------")

cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid") # default ASC(ascending)

items = cursor.fetchall()
for item in items:
    print(item)

print("----------SEPERATOR-----------")

cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC") 

items = cursor.fetchall()
for item in items:
    print(item)

print("----------SEPERATOR-----------")

cursor.execute("SELECT rowid, * FROM customers ORDER BY last_name") 

items = cursor.fetchall()
for item in items:
    print(item)

print("----------SEPERATOR-----------")

cursor.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC") 

items = cursor.fetchall()
for item in items:
    print(item)

connect.commit()

connect.close()

