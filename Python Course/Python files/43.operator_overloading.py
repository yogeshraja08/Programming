# operator overloading - reassign the operator function 

class  A:
    def __init__(self,a):
        self.a=a
        
    def __add__(o1,o2):     # assign addition operator as multiplication
        return o1.a * o2.a
    
    def __pow__(o1,o2):     # assign power operator as addition
        return o1.a + o2.a

o1=A(10)
o2=A(20)
print("total : ",(o1+o2))   # here we use + operator but the o/p will be multiplication

o1=A(3)
o2=A(5)
print("total : ",(o1**o2))  # here we use ** operator but the o/p will be addition