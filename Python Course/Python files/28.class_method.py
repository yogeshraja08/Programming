class student():
    name="yon"
    age=20

    def printall():
        print("name : ",student.name)
        print("age : ",student.age)
student.printall()
print(student.__dict__)

print(getattr(student,"printall"))
getattr(student,"printall")()

print(student.__dict__["printall"]())