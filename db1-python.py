import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin#246$")
mycursor = mydb.cursor()

mycursor.execute("Create database simple")
mycursor.execute("Show databases")

for db in mycursor:
    print(db)