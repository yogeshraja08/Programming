"""
write a program to check the given number is even or odd
"""

a=input("Enter the number : ")
if a.isalpha():
    print("enter numbers only")
else:
    b=int(a)
    if b%2 == 0:
        print(a," is even")
    else:
        print(a," is odd")