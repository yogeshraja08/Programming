print("this is input command")
name=input("enter ur name : ")
print("your name is: " ,name)
print(type(name))


a=float (input("Enter value of A : "))
b=int(input("Enter value of B : "))
c=a+b
print(c)

name1,name2,name3=input("Enter three names with space : ").split()
print("Person 1 : ",name1)
print("Person 2 : ",name2)
print("Person 3 : ",name3)


name1,name2,name3=input("Enter three names with comma : ").split(",")
print("Person 1 : ",name1)
print("Person 2 : ",name2)
print("Person 3 : ",name3)