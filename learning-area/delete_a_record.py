import sqlite3

# Connect to database
connect = sqlite3.connect('customers.db')

cursor = connect.cursor()

cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()
for item in items:
    print(item)

print("----------------SEPERATOR----------------")
cursor.execute("DELETE from customers WHERE rowid = 5") # (5, 'Dan', 'Pas', 'dan@example.com') was deleted.

cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()
for item in items:
    print(item)

connect.commit()

connect.close()

