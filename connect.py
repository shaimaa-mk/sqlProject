import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin#246$")
print(mydb)

if mydb:
    print("Connection Successfully")
else:
    print("Connection Unsuccessfully")
