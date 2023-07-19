user={
    "name":"yogesh",
    "age":20,
    "isMarried":False
}
print(user)
print(type(user))
print(user["name"])
print(user.get("age"))
print(user.keys())  #print only keys
print(user.values())    #print only values
print(user.items()) #print both keys and values

for x in user:
    print(x)
    print(x,"",user[x])

for x in user.values():
    print(x)

for x in user.keys():
    print(x)

for a,b in user.items():
    print(a,b)

if "age" in user:
    print("age is present")

#changing values
user.update({"gender":"male"})
print(user)
user["age"]=21
print(user)
user.pop("age")
print(user)
user.clear()
print(user)
del user
#print(user) #user cannot be printed as it is deleted

user={
    "user1":{
        "name":"yogesh",
        "age":20,
        "isMarried":False
    },
    "user2":{
        "name":"yon",
        "age":21,
        "isMarried":False
    }
}
print(user)