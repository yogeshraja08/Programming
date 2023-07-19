# overriding - reassign the value using inheritance

class employee:
    def workinghrs(self):   # workinghrs has been assigned to 50
        self.hrs = 50
        
    def printhrs(self):
        print("total working hrs : ",self.hrs)

class trainee(employee):
    def workinghrs(self):   # workinghrs has been reassigned to 60
        self.hrs = 60
        
    def resethrs(self):
        super().workinghrs()    # super() is used to access the super class
        
emp = employee()
emp.workinghrs()
emp.printhrs()

trainee = trainee()
trainee.workinghrs()
trainee.printhrs()

trainee.resethrs()
trainee.printhrs()