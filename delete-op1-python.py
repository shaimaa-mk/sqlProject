import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="admin#246$",database="simple")
mycursor = mydb.cursor()
query = "DELETE FROM employee WHERE name = 'adam'"
mycursor.execute(query)
mydb.commit()