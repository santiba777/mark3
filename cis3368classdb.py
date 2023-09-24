import mysql.connector

mydb = mysql.connector.connect(

    host = "cis3368classdb.cebqcn4osxts.us-east-1.rds.amazonaws.com",
    user = "admin",
    password = "alejandro632",
    database = "cis3368classdb"
)

mycursor = mydb.cursor()

mycursor.execute("select * from Sales")

myresults = mycursor.fetchall()

for row in myresults:
    print(row)

