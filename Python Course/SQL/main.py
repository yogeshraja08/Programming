from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="yon", password="Yogesh@08", database="python_db")

if con:
    print("connected")
else:
    print("not connected")

def insertdata(name,age,city):
    res=con.cursor()
    qry="insert into users (name,age,city) values (%s,%s,%s);"
    res.execute(qry,(name,age,city))
    con.commit()
    print("Insertion completed")

def updatedata(name,age,city,id):
    res=con.cursor()
    qry="update users set name=%s , age=%s , city=%s where id=%s ;"
    res.execute(qry,(name,age,city,id))
    con.commit()
    print("Updation completed")

def deletedata(id):
    res=con.cursor()
    qry="delete from users where id=%s ;"
    res.execute(qry,(id,))
    con.commit()
    print("Deletion completed")

def displaydata():
    res=con.cursor()
    qry="select * from users ;"
    res.execute(qry)
    result=res.fetchall()      # fetchall is used to print all records.
    # result=res.execute(qry).fetchone()    # fetchone is used to print first record.
    # result=res.execute(qry).fetchmany(5)   # fetchall is used to print 5 records.
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))
    con.commit()
    print("Data displayed")

options = print("""
    1.Insert
    2.Update
    3.Delete
    4.Display
    5.Exit
""")

while True:
    print(options)
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

    elif c==5:
        quit()

    else:
        print("Enter the correction option")