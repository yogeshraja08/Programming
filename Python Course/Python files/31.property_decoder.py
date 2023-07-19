class user():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # self.msg=self.name + " is " + str(self.age) + " years old."
    @property #property decorator - to call the function without '()'
    def msg(self):
        return self.name + " is " + str(self.age) + " years old."
a=user(input("enter name : "), 25)
print("name : ",a.name)
print("age : ",a.age)
a.age=int(input("enter ur age : "))
print(a.msg)