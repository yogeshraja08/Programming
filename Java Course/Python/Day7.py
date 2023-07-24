arr = input("Enter the list of numbers : ").split(" ")
print(arr)
sum = 0
for i in range(len(arr)):
    sum += int(arr[i])
print("Sum : ",sum)
print("Max : ",max(arr))
print("Min : ",min(arr))