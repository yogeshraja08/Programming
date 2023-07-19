a=input("Enter the number/text : ")
print(a)
print(type(a))
print(id(a))
print("upper case : ",a.upper())
print("lower case : ",a.lower())
print("captalize :",a.capitalize())
print("title : ",a.title())
print("count of 'o' :",a.count("o"))
print("ends with 'ki' : ",a.endswith("ki"))
print("ends with 'sh' : ",a.endswith("sh"))
print("finds 'o' : ",a.find("o"))
print("finds 'o' after 5 strings : ",a.find("o",5))
print("replace 'o' as '0' : ",a.replace("o","0"))
print("is lower case : ",a.islower())
print("is upper case : ",a.isupper())
print("is alpha : ",a.isalpha())
print("is alpha numeric : ",a.isalnum())
print("is numeric : ",a.isnumeric())
print("is decimal : ",a.isdecimal())
print("is space : ",a.isspace())
if a.isspace() :
    print("there is space")
else:
    print("no space") 

b="this\nis\nsplit\nline"
print(b.splitlines())

c="this is split line"
print("this is split line --> ",c.split(" "))

d="this,is,split,line"
print("this,is,split,line --> ",d.split(","))

print(len(a))
print(len(a.strip()))      # removes the blank space before and after the sentence
print(len(a.lstrip()))
print(len(a.rstrip()))

dob = "08-11-2002"
print(dob.partition("-"))

"""
 Y   O   G   E   S   H
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
"""
print("print first index : ",a[0])
print("print last index : ",a[-1])
print("print from first index : ",a[0:])
print("print from first index to 3rd index : ",a[0:3])
print("print upto 3th index : ",a[:4])
print("print upto -2 index : ",a[:-1])
print("print in reverse order : ",a[::-1])
print("print in 3 space order : ",a[::3])
print("print from -1 index to -4th index : ",a[-4:-1])