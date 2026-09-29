import mysql.connector
con=mysql.connector.connect(user="root",password="shabna",host="localhost",database="school_db")
print(con)
c=con.cursor()
query="update student set name=%s where roll_no=%s"
data=('shabna',101)
c.execute(query,data)

con.commit()
if c.rowcount>0:
    print("record updated")
else:
    print("no record found")

