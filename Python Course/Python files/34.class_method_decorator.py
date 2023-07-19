class user():
    count = 0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        user.count += 1     # user.count = user.count + 1

    def printdetails(self):
        print("name : ",self.name,", age : ",self.age)

    @classmethod    # indicates that 'total' is not a general function
    def total(cls):
        return cls.count

a=user("yon", 20)
a.printdetails()
print("total addmisions : ",a.total(),"\n")

b=user("yogesh", 19)
b.printdetails()
print("total addmisions : ",b.total(),"\n")

c=user("yoge", 21)
c.printdetails()
print("total addmisions : ",c.total(),"\n")

print("total no. of addmisions : ",user.total(),"\n")