#list in python
#mutable
#surrounded by []
a=[1,2,3,4,5,6]
print(a)
print(type(a))
c=a.copy()
a.clear()
print(a)
print(c.index(2))

b=[1,True,"yoge",[2,3,4]]
print(b)
print(type(b[0]))
print(type(b[1]))
print(type(b[2]))
print(type(b[3]))
print(b[3])
print(b[3][1])

d=[22,33,22,44,22,55,66]
f=[22,33,22,44,22,55,66]
print(d)
print(max(d))
print(min(d))

d.remove(22) # delete first element '22' in list
print("remove 22 ",d)

print("f : ",f)
f.pop(2)    #delete element in 2nd index in list
print("pop 2 ",f)

d.append(88) #add element to list
print("append 88 ",d)

b.extend(d)  #join the lists
print("extend b from d ",b)

e=["yoge","yogesh","yon"]
print(e)
e.insert(2,"hi") #add element to 2nd index
print("insert hi to 2nd index : ",e)

print(list(range(8)))   #create list that range to 8
print(list("yon"))      #create list with each letters in list

print(d)
d.sort()
print(d)
d.sort(reverse=True)
print(d)

print(e)
e.sort()
print(e)
e.sort(reverse=True)
print(e)
e.sort(key=len)
print(e)