import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="admin#246$",database="simple")
mycursor = mydb.cursor()
mycursor.execute("Show tables")
for tb in mycursor:
    print(tb)