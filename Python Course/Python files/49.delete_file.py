import os
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    # os.rmdir("folder_name")
else:
    print("no file found")