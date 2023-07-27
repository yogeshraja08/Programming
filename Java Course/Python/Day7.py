arr = input("Enter the list of numbers : ").split(" ")
print(arr)
sum = 0
for i in range(len(arr)):
    sum += int(arr[i])
print("Sum : ",sum)
print("Max : ",max(arr))
print("Min : ",min(arr))

print(arr[::-1])

for i in range(len(arr)):
    if int(arr[i]) % 2 == 0:
        print(arr[i],end=" ")
        sum += int(arr[i])
print("sum of even numbers is : ",sum)

sum=0
i=0
while i<=len(arr):
    j=i+1
    while j<=len(arr):
        if int(arr[i]) == int(arr[j]):
            print(arr[i],end=" ")
            sum+=1
print("\nDuplicates : ",sum)