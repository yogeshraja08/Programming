"""
while loop
for loop
"""

i=1
while i<=10:
    print(i)
    i=i+2
print("-------------------")
a=1
while a<=20:
    if a%2==0:
        a=a+1
        continue;
    print(a)
    a=a+1
a=0
while a<=20:
    if a==3:
        a=a+1
        break;
    print(a)
    a=a+1



for i in range(0,10,2):
    print(i)

for a in range(3):
    a=input("enter number 1 : ")
    b=input("enter number 2 : ")
    print(int(a+b))


print("nested loop")
# end="" is used to print the output in same line
for i in range(5):
    for j in range(i):
        print("*",end="")
    print("")

for i in range(8,0,-1):
    for j in range(i):
        print("*",end="")
    print("")


#ASCII values
# A-Z => 65-90
# a-z => 97-122

for i in range(65,91,1):
    print(chr(i),end="")


# else in while loop
i=1
while i<=20:
    if i%5==0 or i%2==0:
        i=i+1
        continue;
    print(i)
    i=i+1
else:
    print("finished!")


# else in for loop
for i in range(10):
    i=i+1
    print(i)
else:
    print("finished!")