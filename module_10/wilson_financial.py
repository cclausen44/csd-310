# Rufino Tzunun 
# Christopher Clausen 
# Moises Herrera 
# 7/07/2022 
# Module 10.2 
# Team Delta 
# Wilson Financial

import mysql.connector

config = {
    "user": "root",
    "password": "GOTg5913!!",
    "host": "127.0.0.1",
    "database": "w_financial",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

# create employee table
cursor.execute("CREATE TABLE Employees (emp_id INTEGER NOT NULL, emp_fname CHAR(30) NOT NULL, emp_lname VARCHAR(30) NOT NULL, emp_pos CHAR(30) NOT NULL)")
# insert values into employee table
cursor.execute("INSERT INTO Employees(emp_id, emp_fname, emp_lname, emp_pos) VALUES('001', 'Phoenix', 'Two Star', 'Secretary')")
cursor.execute("INSERT INTO Employees(emp_id, emp_fname, emp_lname, emp_pos) VALUES('002', 'June', 'Santos', 'Compliance Manager')")

# create client table
#cursor.execute("CREATE TABLE Client (cl_id INTEGER NOT NULL, cl_name CHAR(30) NOT NULL, cl_address CHAR(50) NOT NULL, cl_phone CHAR(10) NOT NULL, cl_email CHAR(50) NOT NULL)")
# insert values into client table
"""
cursor.execute("INSERT INTO Client (cl_id, cl_name, cl_address, cl_phone, cl_email) VALUES ")
cursor.execute("INSERT INTO Client (cl_id, cl_name, cl_address, cl_phone, cl_email) VALUES ")
cursor.execute("INSERT INTO Client (cl_id, cl_name, cl_address, cl_phone, cl_email) VALUES ")
cursor.execute("INSERT INTO Client (cl_id, cl_name, cl_address, cl_phone, cl_email) VALUES ")
cursor.execute("INSERT INTO Client (cl_id, cl_name, cl_address, cl_phone, cl_email) VALUES ")
cursor.execute("INSERT INTO Client (cl_id, cl_name, cl_address, cl_phone, cl_email) VALUES ")
cursor.execute("INSERT INTO Client (cl_id, cl_name, cl_address, cl_phone, cl_email) VALUES ")
cursor.execute("INSERT INTO Client (cl_id, cl_name, cl_address, cl_phone, cl_email) VALUES ")
"""
# create transactions table
#cursor.execute("CREATE TABLE Transactions (cl_id INTEGER NOT NULL, order_id INTEGER NOT NULL, order_date VARCHAR(10) NOT NULL, order_price INTEGER NOT NULL)")
# insert values into transactions table
"""
cursor.execute("INSERT INTO Transactions (order_id, order_date, order_price) VALUES ")
cursor.execute("INSERT INTO Transactions (order_id, order_date, order_price) VALUES ")
cursor.execute("INSERT INTO Transactions (order_id, order_date, order_price) VALUES ")
cursor.execute("INSERT INTO Transactions (order_id, order_date, order_price) VALUES ")
cursor.execute("INSERT INTO Transactions (order_id, order_date, order_price) VALUES ")
cursor.execute("INSERT INTO Transactions (order_id, order_date, order_price) VALUES ")
cursor.execute("INSERT INTO Transactions (order_id, order_date, order_price) VALUES ")
cursor.execute("INSERT INTO Transactions (order_id, order_date, order_price) VALUES ")
cursor.execute("INSERT INTO Transactions (order_id, order_date, order_price) VALUES ")
cursor.execute("INSERT INTO Transactions (order_id, order_date, order_price) VALUES ")
cursor.execute("INSERT INTO Transactions (order_id, order_date, order_price) VALUES ")
"""
# Display Tables
# display employee records
cursor.execute("SELECT emp_id, emp_fname, emp_lname, emp_pos FROM Employees")
print("--DISPLAYING EMPLOYEE RECORDS--")
Employees = cursor.fetchall()
for employee in Employees:
    print("Employee ID: {}".format(employee[0]),
        "\nFirst Name: {}".format(employee[1]),
        "\nLast Name: {}".format(employee[2]),
        "\nPosition: {}\n".format(employee[3]))
"""
# display client records
cursor.execute()
print("-DISPLAYING CLIENT RECORDS--")
Client = cursor.fetchall()
for clients in Client:
    print("Client ID: {}".format(clients[0]),
        "\nName: {}".format(clients[1]),
        "\nAddress: {}".format(clients[2]),
        "\nPhone: {}\n".format(clients[3]),
        "\nEmail: {}\n".format(clients[4]))

# display transaction records
cursor.execute()
print("--DISPLAYING TRANSACTION RECORDS--")
for transaction in Transactions:
    print("")
"""