# types of exception in python
"""
print(dir(locals()["__builtins__"]))
print("total no of build-in exceptions : ",len(dir(locals()["__builtins__"])))

try:
    print(a)
except NameError as e:
    print(e)
    print("A is not defined")

try:
    print(10/0)
except ZeroDivisionError:
    print("denominator can not be zero!")

try:
    file=open("test.py")
except FileNotFoundError as e:
    print(e)
else:
    print(file.read())

"""

# multiple exceptions
try:
    a=10/20
    print(a)
    b=[1,2,3,4]
    print(b[8])
except ZeroDivisionError as a:
    print(a)
except IndexError as b:
    print(b)
else:
    print("program terminated!")