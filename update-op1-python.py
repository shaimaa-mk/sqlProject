import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="admin#246$",database="simple")
mycursor = mydb.cursor()
query = "UPDATE employee SET salary = 80000 WHERE name = 'fatiam'"
mycursor.execute(query)
mydb.commit()