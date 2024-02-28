ip = input("Enter the number / word : ")
arr = [*ip]
for i in range(len(arr)//2):
    print(arr[i],end="")
newArr = arr[::-1]
for i in range((len(newArr)//2)+1):
    print(newArr[i],end="")