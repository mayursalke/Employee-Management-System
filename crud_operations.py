import mysql.connector

def connect_to_db():
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rude/1999',
        database='Employee',

    )
    return database

# REGISTER NEW EMPLOYEE
def register(name, address,contact, password):
    database = connect_to_db()
    cursor = database.cursor()

    query = "INSERT INTO Employee (Employee_Name, Address, Contact, PASSWORD) VALUES (%s, %s, %s,%s)"
    values = (name, address, contact, password)

    cursor.execute(query, values)
    database.commit()
    cursor.close()
    database.close()

    print("Thank you for registering")

def Login(Employee_ID, password):
    database = connect_to_db()
    cursor = database.cursor()

    query = "SELECT * FROM Employee WHERE Employee_ID = %s AND PASSWORD = %s"
    cursor.execute(query, (Employee_ID, password))

    employee = cursor.fetchone()
    cursor.close()

    return employee


# Updating detail of employee

def update_detail(Employee_ID, column, new_value):
    database = connect_to_db()
    cursor = database.cursor()

    query = f"UPDATE Employee SET {column} = %s WHERE Employee_ID = %s"
    cursor.execute(query, (new_value, Employee_ID))

    database.commit()
    cursor.close()
    database.close()

    print("Your details have been updated")

# DELETE AN EMPLOYEE 

def delete_employee(Employee_ID):
    database = connect_to_db()
    cursor = database.cursor()

    query = "DELETE FROM Employee WHERE Employee_ID = %s"
    cursor.execute(query, (Employee_ID,))

    database.commit()
    cursor.close()
    database.close()

    print("Employee Details deleted succesfully")

# Read all Employee (Only id and name using)

def read_all():
    database = connect_to_db()
    cursor = database.cursor()

    query = "SELECT Employee_ID, Employee_Name FROM Employee"
    cursor.execute(query)

    employee = cursor.fetchall()
    cursor.close()
    database.close()

    return employee

# Read specific Employee details by employee id
def read_employee(Employee_ID):
    database = connect_to_db()
    cursor = database.cursor()

    query = "SELECT * FROM Employee WHERE Employee_ID =%s"
    cursor.execute(query, (Employee_ID))

    emplyee = cursor.fetchone()
    cursor.close()
    database.close()

    return emplyee

