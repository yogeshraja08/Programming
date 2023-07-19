# ABC - Abstract Base Class
# Abstract class - doesn't have any definition(def) and that will be redefined in child class
from abc import ABC, abstractmethod
class bank(ABC):
    @abstractmethod
    def loan(self):
        pass
    
    @abstractmethod
    def credit(self):
        pass
    
    @abstractmethod
    def debit(self):
        pass
    
class hdfc(bank):
    def loan(self):
        print("provide loan")
    
    def credit(self):
        print("provide credit")
    
    def debit(self):
        print("provide debit")
        
    def card(self):
        print("provide card")

o=hdfc()
o.loan()
o.credit()
o.debit()
o.card()