import sqlite3

# Connect to database
connect = sqlite3.connect('customers.db')

cursor = connect.cursor()

cursor.execute("SELECT rowid, * FROM customers")

"""
cursor.fetchone() LAST ITEM
cursor.fetchmany(number) FETCHES number ITEMS
cursor.fetchall()
"""

items = cursor.fetchall()
for item in items:
    print(item)
# you can get a better output usinh loops, \t, \n, etc.

connect.commit()

connect.close()

