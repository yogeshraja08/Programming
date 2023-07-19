# try block in python
a=int(input("enter value of A : "))
b=int(input("enter value of B : "))
try:
    c=a/b
except Exception as e:
    print(e)
else:
    print("value of c is : ",c)
finally:
    print("program completed!")