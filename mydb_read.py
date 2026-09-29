# connect set cheyya
import mysql.connector
con=mysql.connector.connect(user="root",password="shabna",host="localhost",database="school_db")
print(con)

#cursor function set aaka
c=con.cursor()
query="select * from student"
c.execute(query)



records=c.fetchall()
if records:
    for row in records:
        print(row)
else:
    print("no records found")
c.close()
con.close()

