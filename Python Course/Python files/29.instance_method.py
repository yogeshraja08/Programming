class student():
    name="yon"
    age=20

    def printall(self):     # instance method - assign keys ('self') to the function
        print("name : ",student.name)
        print("age : ",student.age)
a=student()
a.printall()

student.printall(a)


class stu():
    name="yon"
    age=20

    def printstu(self,gender):
        print("name : ",student.name)
        print("age : ",student.age)
        print("gender : ",gender)
b=stu()
b.printstu("male")
stu.printstu(b,"male")