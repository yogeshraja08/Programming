class student():
    name="yogesh"
    age=20

# 'getattr method' to acces the class
print(getattr(student,"name"))
print(getattr(student,"age"))
print(getattr(student,"gender","attribute not found"))

# 'dot notation' to access the class
print(student.name)
print(student.age)

# setattr - update class
setattr(student,"name","yon")
print(student.name)

setattr(student,"gender","male")
print(student.gender)

student.city="erode"
print(student.city)

# delete attr in class
print(student.__dict__)
delattr(student,"city")
print(student.__dict__)
del student.age
print(student.__dict__)

print(student)
del student
# print(student)    #can not be printed as the class is deleted
