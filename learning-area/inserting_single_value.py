import sqlite3

# Connect to database
connect = sqlite3.connect('customers.db')

cursor = connect.cursor()

cursor.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@example.com')")

connect.commit()

connect.close()

