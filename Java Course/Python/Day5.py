# a = "yogesh"
# print(a.index("g"))
# print(a[0].upper(),end="")
# print(a[1:])

#   # palindrome
# word = input("Enter the word : ")
# rev = word[::-1]
# # arr = list(word)
# # rev = ""
# # for i in range (len(arr)-1,-1,-1):
# #     rev += arr[i]
# if (rev==word):
#     print("It is palindrome")
# else:
#     print("It is not palindrome")

# # find vowels
# word = input("Enter the word : ")
# arr = list(word)
# vowels = ['a','e','i','o','u']
# count = 0
# for i in range(len(arr)):
#     if (arr[i] in vowels):
#         count+=1
# print(count)

# anagram
word1 = input("Enter the word 1 : ")
word2 = input("Enter the word 2 : ")
arr1 = list(word1)
arr2 = list(word2)
count = 0
if len(arr1) == len(arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if (arr1[i]==arr2[j]):
                count+=1
                break
if count == len(arr1):
    print("It is anagram")
else:
    print("It is not anagram")