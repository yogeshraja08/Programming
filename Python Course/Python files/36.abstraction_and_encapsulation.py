"""
Data Abstraction :
    It refers to providing only essential information to the outside world and hiding their background details.
    To represent the needed information in program without presenting the details.

Data Encapsulation :
    It is a process of wraping code and data together into a single unit.
"""

class libr():
    def __init__(self,books):
        self.books=books

    def list_books(self):
        print("available books")
        for book in self.books:
            print(book)
    
    def borrow_books(self,borrow_books):
        if borrow_books in self.books:
            print("get ur books ")
            self.books.remove(borrow_books)
        else:
            print("book not available")

    def receive_books(self,receive_books):
        print("you have returned the book")
        self.books.append(receive_books)

books=["c","c++","java","python"]
a=libr(books)

msg= """
    1.display book
    2.borrow book
    3.return book
    4.exit
"""

while True:
    print(msg)
    ch=int(input("enter ur choise : "))
    if ch==1:
        a.list_books()
    elif ch==2:
        book=input("enter the book name : ")
        a.borrow_books(book)
    elif ch==3:
        book=input("enter the book name : ")
        a.receive_books(book)
    elif ch==4:
        print("thank you")
        break
    else:
        print("you have entered a wrong option")
        quit()   # 'break' can also be used