# multiple inheritance
class father:
    def fishing(self):
        print("knows fishing")

    def chess(self):
        print("knows to play chess (pro player)")

class mother:
    def cook(self):
        print("knows cooking ")

    def chess(self):
        print("knows to play chess")

class son(father,mother):
    def cycling(self):
        print("knows cycling")

a=son()
a.cycling()
a.fishing()
a.cook()
a.chess()   # both class has chess function but only the first class will be printed