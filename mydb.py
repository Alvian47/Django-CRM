# pip install mysql
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password='mysql47'
)

cursorObject = database.cursor()

cursorObject.execute("create database elderco")

print("All done")
