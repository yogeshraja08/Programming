try:
    file=open("text.txt","a")       # 'a' - Add the content in the file
    file.write("\n by Yogesh")      # 'write' - used to write content
    file.close()
    
    file=open("text.txt","r")
    print(file.read())
    
except FileNotFoundError as e:
    print(e)
    
else:
    file.close()