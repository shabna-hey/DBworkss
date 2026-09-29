import mysql.connector
#
#
#
# con=mysql.connector.connect(user="root",password="shabna",host="localhost")
# #it returns connection object
# print(con)
# #
# #
# # #cursor object -- for executing sql quries
# c=con.cursor()
# #query for creating db file
# query="create database if no exists school_db"
# c.execute(query)
# print("database file created")
#
# c.close()
# con.close()









#create table



con=mysql.connector.connect(user="root",password="shabna",host="localhost",database="school_db")

c=con.cursor()
#insert into table
# query="""create table if not exists student(roll_no int not null primary key,
#        name varchar (20),
#        age int,
#        place varchar(20),
#        phone varchar(20),
#        total_mark int
#        )"""
# c.execute(query)
# print("table created")
# c.close()
# con.close()


#create new records/insertion data into data base table student

query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s),(%s,%s,%s,%s,%s,%s)"
data=(101,'anu',23,'ernk',1234567789,78),(102,'arun',45,'malp',34959299,90)


c.execute(query,data)
con.commit() #permenently saves data into database
print("inserted data successfully")
c.close()
con.close()
