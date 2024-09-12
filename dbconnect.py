import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rude/1999"
)

#preparing a cursor object
cursorObject = database.cursor()

# creating database
cursorObject.execute("CREATE DATABASE Employee")