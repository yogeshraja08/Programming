class student():
    def __init__(self,total):
        self._total=total   # '_total' --> act as private  ( _ indicate that it is private)
    def average(self):
        return self._total / 5

    @property   # getter function
    def total(self):
        return self._total

    @total.setter
    def total(self,t):
        if t<0 or t>500:
            print("enter the correct total!")
        else:
            self._total = t

a=student(429)
print("total : ",a.total)
print("average : ",a.average())
a.total=427
print("total : ",a.total)
print("average : ",a.average())