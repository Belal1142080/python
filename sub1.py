import mysql.connector
mydb= mysql.connector.connect(host="localhost", user="belal", passwd="b4181171100069121B", database="mydatabase")
mycursor= mydb.cursor()
mycursor.execute("select * from student")

for i in mycursor:
	print(i)
