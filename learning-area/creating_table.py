import sqlite3

connect = sqlite3.connect('customer.db')

cursor = connect.cursor()

cursor.execute("""CREATE TABLE customers (
            first_name text,
            last_name text,
            email text
        )""")

connect.commit()