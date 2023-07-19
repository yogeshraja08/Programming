class user():
    def __init__(self,name):
        print("constructor method")
        self.name= name
    def printall(self):
        print("name : ",self.name)

a=user("yogesh")
a.printall()
print(a.__dict__)

b=user("yon")
b.printall()
print(b.__dict__)