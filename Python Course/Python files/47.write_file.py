try:
    file=open("text.txt","w")       # 'write' - overwrite the content in the file
    file.write("Welcome to the Python programing")      # 'write' - used to write content
    file.close()
    
    file=open("text.txt","r")
    print(file.read())
    
except FileNotFoundError as e:
    print(e)
    
else:
    file.close()