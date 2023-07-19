#tuple in python
#immutable
#surrounded by ()

a=(1,2,4,True,"yoge")
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[1:3])

b=list(a)
print(b)
b.append(2) #error not condsidered
print(b)
print(type(b))
a=tuple(b)
print(b)

for i in a:
    print(i)

if "yoge" in a:
    print("founded")
else:
    print("not found")
print(len(a))

a=(1)
print(type(a))
a=(1,)
print(type(a))

del a
a=(1,2,8,4)
b=(0,9,8,7)
c=a+b
print(c)
print(c.count(8))

c=(a,b) #nested tuple
print(c)

x=("yon",)*5
print(x)

print(min(a))
print(max(a))
