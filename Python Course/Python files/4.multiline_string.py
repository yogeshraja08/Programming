para=["name1","love","name2"]
print("❤".join(para))

para=[1,2,3]
print(para)
print(para[0])
print(para[1])
print(para[2])

para=[]
print("enter a para : ")
while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
print(para)
output=". ".join(para)
print(output)