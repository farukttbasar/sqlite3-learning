import database

database.create_table()

i = int(input("How many customers do you want to add > "))

for _ in range(i):
    first = input("First Name? > ") 
    last = input("Last Name? > ")
    email = input("Email? > ")
    age = int(input("Age? > "))
    database.add_one(first, last, email, age)

database.show_all()
