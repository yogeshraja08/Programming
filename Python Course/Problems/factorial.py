number = int(input("Enter the number : "))
factorial = 1
for i in range(number):
    factorial = factorial * (i+1)
print(factorial)