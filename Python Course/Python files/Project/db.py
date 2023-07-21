import sqlite3

class database:
    def __init__(self,db):
        self.con = 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        sqlite3.connect(db)
        self.cur = self.con.cursor()
        qry = """ 
            create table if not exists staff (
                id integer primary key,
                name text,
                age text,
                doj text,
                email text,
                gender text,
                contact text,
                address text
            )
        """
        self.cur.execute(qry)
        self.con.commit()
        
    # insert function
    def insert(self,name,age,doj,email,gender,contact,address):
        qry = "insert into staff values (NULL,?,?,?,?,?,?,?)"
        self.cur.execute(qry,(name,age,doj,email,gender,contact,address))
        self.con.commit()
        
    # fetch all data from db
    def fetch(self):
        qry = "select * from staff"
        self.cur.execute(qry)
        rows = self.cur.fetchall()
        return rows
        
    # delete record in db
    def delete(self,id):
        qry = "delete from staff where id=?"
        self.cur.execute(qry,(id,))
        self.con.commit()
        
    # update record in db
    def update(self,id,name,age,doj,email,gender,contact,address):
        qry = "update staff set name=? , age=? , doj=? , email=? , gender=? , contact=? , address=? where id=? "
        self.cur.execute(qry,(name,age,doj,email,gender,contact,address,id))
        self.con.commit()