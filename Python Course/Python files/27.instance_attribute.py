# instance - store the value temporaryly
class user():
    course="python"
a=user()
print(user.__dict__)
print(user.course)
print(a.__dict__)
print(a.course)
a.course="html" # 'html' stores in variable 'a' not in class 'user'
print(a.course)

b=user()
print(b.course)