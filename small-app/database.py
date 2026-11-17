import sqlite3

def create_table():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS customers (
            first_name text,
            last_name text,
            email text,
            age integer
        )""")

    conn.commit()
    conn.close()

def add_one(first, last, email, age):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES (?, ?, ?, ?)", (first, last, email, age))

    conn.commit()
    conn.close()

def delete_one(rowid):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("DELETE FROM customers WHERE rowid = (?)", (rowid,))

    conn.commit()
    conn.close()

def show_all():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()



    



