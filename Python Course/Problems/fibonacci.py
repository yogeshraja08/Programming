number = int(input("Enter the number : "))
n1=0
n2=1
print(n1)
print(n2)
for i in range(number):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3