import mysql.connector
con=mysql.connector.connect(user="root",password="shabna",host="localhost",database="school_db")
print(con)

#cursor function set aaka
c=con.cursor()
query="delete from student where roll_no=%s"
data=(102,)
c.execute(query,data)
con.commit()


if c.rowcount>0:
    print("data is delete")
else:
    print(" no data found")
