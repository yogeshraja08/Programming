class user():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def printdetails(self):
        print("name : ",self.name,", age : ",self.age)

    @staticmethod   # no need to assign key ('self') to the function
    def welcome():
        print("welcome!")

a=user("yon", 20)
a.printdetails()
a.welcome()

b=user("yogesh", 19)
b.printdetails()
b.welcome()