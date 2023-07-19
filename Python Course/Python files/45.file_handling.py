try:
    file=open("text.txt","r")
    print(file.read())

except FileNotFoundError as e:
    print(e)

else:
    file.close()

file=open("1.basic.py","r")
print(file.readline())  # reads the first line only
print(file.readline())  # reads the second line only
print(file.readline())  # reads the third line only
print(file.readline(5))  # reads the first five character of fourth line

file=open("2.python_keywords.py","r")
print(file.readlines())     # reads the entire file and converts each line to list