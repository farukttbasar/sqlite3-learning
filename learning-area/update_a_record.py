import sqlite3

# Connect to database
connect = sqlite3.connect('customers.db')

cursor = connect.cursor()

cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()
for item in items:
    print(item)

print("----------------SEPERATOR----------------")
cursor.execute("""UPDATE customers SET first_name = "Micheal"
                WHERE rowid = 2
""")

cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()
for item in items:
    print(item)

connect.commit()

connect.close()

