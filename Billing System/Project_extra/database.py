import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="pi",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO shop (name, phone_no, email, balance) VALUES (%s, %s, %s, %s)"
val = [
  ('yuvraj', 7347335050, "yuvrajbansal3396@gmail.com", 1200),
  ('shravel', 8222835581, "shravelrishyan@gmail.com", 0),
  ('sohil', 9996665842, "nagpal.sn12@gmail.com", 200)
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")