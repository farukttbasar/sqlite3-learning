import sqlite3

# Connect to database
connect = sqlite3.connect('customers.db')

cursor = connect.cursor()

customers = [
    ('Wes', 'Brown', 'wes@example.com'),
    ('Steph', 'Kuewa', 'steph@example.com'),
    ('Dan', 'Pas', 'dan@example.com'),
]

cursor.executemany("INSERT INTO customers VALUES (?,?,?)", customers)

connect.commit()

connect.close()

