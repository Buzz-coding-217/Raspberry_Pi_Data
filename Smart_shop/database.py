import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="pi",
  database="mydatabase"
)

mycursor = mydb.cursor()
print("All Account")
print("============")
sql = "SELECT * FROM shop"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
