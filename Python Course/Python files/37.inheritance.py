"""
Inheritance
    It is a process in which one object acquires all the properties and behaviour of its parent object automatically.
"""

"""
single inheritance :
    It is defined as the inheritance in which a derived class is inherited from the only one base class.
"""
# eg:
class parent():
    pass    # pass is used to bypass the class because class shold not be empty
class son(parent):
    pass


"""
multiple inheritance :
    It is a feature of object oriented concept, where a class can inherit properties of more than one parent class.
"""
# eg:
class father():
    pass
class mother():
    pass
class son(father,mother):
    pass


"""
mutilevel inheritance :
"""
# eg:
class grandfather():
    pass
class father(grandfather):
    pass
class son(father):
    pass