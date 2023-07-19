def welcome():
    print("welcome to function programing in python")

welcome()
welcome()

# No return type without argument function in python
def add():
    a=int(input("enter a : "))
    b=int(input("enter b : "))
    c=a+b
    print(c) # no return as it is printed
add()   # without argument

# No return type with argument function in python
def sub(a,b):
    c=a-b
    print(c)    # no return
sub(20,4)   # with arguments as it is printed

# return type without argument function in python
def mul():
    a=int(input("enter a : "))
    b=int(input("enter b : "))
    c=a*b
    return c    # returned as it is not printed
x=mul() # with arg
print(x)

# return type with argument function in python
def div(a,b):
    c=a/b
    return(c)    # returned as it is not printed
y=div(20,4) # without arguments 
print(y)

# arrbitrary arguments functions in python (*)
def class_12(*students):
    print(students)
class_12("yoge","yon","you","me")

# keyword arguments function in python 
def message(name,age):
    print(name,"'s age is ",age)
message(20,"yon")

def msg(name,age):
    print(name,"'s age is ",age)
message(age=20,name="yon")

# arrbitrary keywords functions in python (**)
def biodata(**data):
    print(data)
biodata(name="yon",age=20,gender="male")

# default parameter function in python
def user(name,city="salem"):
    print(name,"is from ",city)
user("yoge","dharmapuri")
user("yon","erode")
user("you")

# passing a list as an argument in function python
def total(marks):
    return sum(marks)
print("total : ",total([20,30,24]))

# recursive function - function that call itself to complete the function
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
a=factorial(5)
print(a)
"""
# ececution of the above function
factorial(5)
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1
"""

c=lambda a:a+10
print(c(5))

c=lambda a,b:a*b
print(c(10,20))