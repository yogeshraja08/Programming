print("hello world")
check = 1
while check == 1:
    num = int(input("Enter the number : "))
    for i in range(16):
        print(i,"*",num,"=",i*num)
        i=i+1
    check = int(input("If you want to continue, Press '1' or else Press '0' \n\t"))

name1 = input("Enter the name 1 : ")
name2 = input("Enter the name 2 : ")
print(name1," and ",name2," are friends....")