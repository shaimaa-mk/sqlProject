import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="admin#246$",database="simple")
mycursor = mydb.cursor()
# mycursor.execute("select name from employee")
# result = mycursor.fetchone()
mycursor.execute(("Select * from employee"))
result = mycursor.fetchall()
for row in result:
    print(row)