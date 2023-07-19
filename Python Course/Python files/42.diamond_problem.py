"""
# diamond problem
            A
            |
         -------    
        |       |   
        B       C
        |       |   
        ---------    
            |
            D
"""

class A:
    def display(self):
        print("display A")
        
class B(A):
    def display(self):
        print("display B")
        
class C(A):
    def display(self):
        print("display C")
        
class D(B,C):
    def display(self):
        print("display D")
        
o = D()
o.display()