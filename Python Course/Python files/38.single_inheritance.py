# single inheritance
class nokia:
    company = "nokia india"
    website = "www.nokia.in"

    def contact_details(self):
        print("address : tamilnadu")

class nokia1100(nokia): # nokia1100 is class that inherited from class nokia 
                        # any attributes in nokia can be accessed from nokia1100
    def __init__(self):
        self.name = "nokia 1100"
        self.year = 1990
    
    def product_details(self):
        print("name : ",self.name)
        print("year : ",self.year)
        print("company : ",self.company)
        print("website : ",self.website)

mobile=nokia1100()
mobile.product_details()
mobile.contact_details()