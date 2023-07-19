import sqlite3

connection=sqlite3.connect("D:\Documents\python course\database\database.db")

def insertdata(name,age,city):
    qry="insert into users (name,age,city) values (?,?,?);"
    connection.execute(qry,(name,age,city))
    connection.commit()
    print("Insertion completed")
    
def updatedata(name,age,city,id):
    qry="update users set name=? , age=? , city=? where id=? ;"
    connection.execute(qry,(name,age,city,id))
    connection.commit()
    print("Updation completed")

def deletedata(id):
    qry="delete from users where id=? ;"
    connection.execute(qry,(id))
    connection.commit()
    print("Deletion completed")

def displaydata():
    qry="select * from users ;"
    result=connection.execute(qry)
    for row in result:
        print(row)
    connection.commit()
    print("Data displayed")

options = ("""
    1.Insert
    2.Update
    3.Delete
    4.Display
""")
print(options)

ch=1
while ch==1:
    c=int(input("Select your choise : "))
    if c==1:
        name=input("Enter name : ")
        age=input("Enter age : ")
        city=input("Enter city : ")
        insertdata(name, age, city)
    elif c==2:
        id=input("Enter ID : ")
        name=input("Enter name : ")
        age=input("Enter age : ")
        city=input("Enter city : ")
        updatedata(name,age,city,id)
    elif c==3:
        id=input("Enter ID : ")
        deletedata(id)
        
    elif c==4:
        displaydata()
    else:
        print("Enter the correction option")
    ch=int(input("Enter 1 to continue : "))
    print(options)

print("Thankyou")