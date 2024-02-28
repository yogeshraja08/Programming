  # palindrome
word = input("Enter the word : ")
rev = word[::-1]
# arr = list(word)
# rev = ""
# for i in range (len(arr)-1,-1,-1):
#     rev += arr[i]
if (rev==word):
    print("It is palindrome")
else:
    print("It is not palindrome")