a=[1,2]
b=[1,2]
c=a
print(id(a))
print(id(b))
print(id(c))
print(a is c)   #id of a and c are equal
print(a is b)   #id of a and b are not equal
print(a is not c) 
print(a is not b)