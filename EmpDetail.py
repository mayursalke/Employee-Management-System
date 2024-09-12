import mysql.connector

# Reconnecting to the 'Employee' database
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rude/1999",
    database="Employee"  # Specify the database to use
)

cursorObject = database.cursor()

# Creating a table Employee

query_to_create_table = """
CREATE TABLE Employee (
Employee_ID INTEGER AUTO_INCREMENT PRIMARY KEY,
Employee_Name VARCHAR(255) NOT NULL,
Address VARCHAR(255) NOT NULL,
Contact VARCHAR(255) NOT NULL,
PASSWORD VARCHAR(255) NOT NULL
)
"""

cursorObject.execute(query_to_create_table)

print("Employee Table created successfully")
