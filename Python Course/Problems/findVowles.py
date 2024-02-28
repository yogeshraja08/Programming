# find vowels
word = input("Enter the word : ")
arr = list(word)
vowels = ['a','e','i','o','u']
count = 0
for i in range(len(arr)):
    if (arr[i] in vowels):
        count+=1
print(count)