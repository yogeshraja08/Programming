try:
    file=open("text.txt","r")
    for line in file:
        print(line)
    
except FileNotFoundError as e:
    print(e)
    
else:
    file.close()