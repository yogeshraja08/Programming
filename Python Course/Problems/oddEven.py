number = int(input("Enter the number : "))
factor = 0
for i in range(number):
    if (number%2==0):
        factor+=1
if factor==1:
    print(number," is a even number.")
else:
    print(number," is not a even number.")