import sqlite3

# Connect to database
connect = sqlite3.connect('customers.db')

connect.commit()

connect.close()

