names={"yon","yogesh","python"}
print(names)
print(type(names))

#access values using for loop
for name in names:
    print(name)

#addng new element
names.add("don")
print(names)

#update another set of data
a={"it","is","new","name"}
names.update(a)
print(names)
names.remove("new") #remove if it contains the value or else there will be error #note: case sensitive
print(names)
names.discard("YoN") #remove if it contains the value or else there will be no error
print(names)
names.pop() #remove a random value
print(names)
names.clear() #delete all values in set
print(names)
del names #delete the set
# print (names) #name cannot be printed as it is deleted

names={"yon","yogesh","python","yon"} #values can not be duplicated in set
print(names)


a={1,2,3,4}
b={5,4,7,8}
c=a.union(b)
print(c)
c=a.update(b)
print(a)

a={1,2,3,4}
b={5,4,7,8}
c=a.intersection(b)
print(c)
c=a.update(b)
print(c)