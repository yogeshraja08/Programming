# start = int(input("number 1 : "))
# end = int(input("number 2 : "))
# for start in range(end):
#     print(start)
#     start+=1

number = int(input("Enter the number : "))

"""condition for prime number"""
# factor = 0
# for i in range(number):
#     if (number%2==0):
#         factor+=1
# if factor==1:
#     print(number," is a prime number.")
# else:
#     print(number," is not a prime number.")

n1=0
n2=1
for i in range(number):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3