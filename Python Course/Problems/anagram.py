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