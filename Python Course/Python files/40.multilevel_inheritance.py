# multilevel inheritance
class grandfather():
    def house(self):
        print("grandfa's house")

class father(grandfather):
    def bike(self):
        print("father's bike")
class son(father):
    def ps5(self):
        print("son's PS5")

a=son()
a.ps5()
a.bike()
a.house()