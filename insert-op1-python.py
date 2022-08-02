import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="admin#246$",database="simple")
mycursor = mydb.cursor()
sqlform = "insert into employee (name,salary) values (%s,%s)"
employees = [("adam",20000),("fatiam",30000),("alaa",10000),]
mycursor.executemany(sqlform,employees)
mydb.commit()