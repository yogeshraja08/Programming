print("WELCOME TO THE FIRST PROGRAM BY YoN")
name=str(input("Enter your name : "))
if name=="yon" or name=="yogesh" or name=="Yogesh":
    print("hello yon")
else:
    age=int(input("enter your age : "))
    if age>20:
        print("Hi ",name,"!\nyou are elder than YON")
    elif age==20:
        print("Hi ",name,"!\nyou and YoN are at same age")
    else:
        print("Hi ",name,"!\nyou are younger than YON")

print("\nlet's get into the program\n")

import datetime as dt

class libr():
    def __init__(self,books):
        self.books=books

    def list_books(self):
        print("Available books")
        for book in self.books:
            print(book)
    
    def borrow_books(self,borrow_books):
        if borrow_books in self.books:
            print("Get ur book")
            today=dt.date.today()
            duedate=today + dt.timedelta(days=15)
            print("Due date : ",duedate)
            self.books.remove(borrow_books)
        else:
            print("Book not available")

    def receive_books(self,receive_books):
        dueday,duemonth,dueyear=input("Enter the due date : ").split("-")
        duedays=int(dueyear) * 10000 + int(duemonth) * 100 + int(dueday)
        today=dt.date.today()
        td=int(today.year) * 10000 + int(today.month) * 100 + int(today.day)
        due=td-duedays
        print("Delayed days : ",due)
        for receive_books in range(3):
            if due<=0:
                print("You have returned the book on time.")
                print("Now the book was added to the list")
                print("Thankyou for using YoN book management service!\n")
            elif due>0 and due<=5:
                print("fine amount for ",due,"days is : ",due*2)
                pay=input("are you willing to pay now (Y/N) : ")
                if pay=="Y" or pay=="y":
                    print("scan the QR code")
                    for i in range(8):
                        for j in range(20):
                            print("*",end="")
                        print("")
                    print("Now the book was added to the list")
                    print("Thankyou for using YoN book management service!")
                    break;
                elif pay=="N" or pay=="n":
                    returnday=input("When will you return the book?\n")
                    print("Return the book ASAP.....")
                    print("Thankyou for using YoN book management service!")
                    break;
                else:
                    print("Enter the correct option")
                    continue;
            elif due>5 and due<=15:
                print("Fine amount for ",due,"days is : ",due*3)
                pay=input("Are you willing to pay now (Y/N) : ")
                if pay=="Y" or pay=="y":
                    print("Scan the QR code")
                    for i in range(8):
                        for j in range(20):
                            print("*",end="")
                        print("")
                    print("Now the book was added to the list")
                    print("Thankyou for using YoN book management service!")
                    break;
                elif pay=="N" or pay=="n":
                    returnday=input("When will you return the book?\n")
                    print("Return the book ASAP.....")
                    print("Thankyou for using YoN book management service!")
                    break;
                else:
                    print("Enter the correct option")
                    continue;
            elif due>15 and due<=30:
                print("Fine amount for ",due,"days is : ",due*5)
                pay=input("Are you willing to pay now (Y/N) : ")
                if pay=="Y" or pay=="y":
                    print("Scan the QR code")
                    for i in range(8):
                        for j in range(20):
                            print("*",end="")
                        print("")
                    print("Thankyou for using YoN book management service!")
                    print("Now the book was added to the list")
                    break;
                elif pay=="N" or pay=="n":
                    returnday=input("When you will return the book?\n")
                    print("Return the book ASAP.....")
                    print("Thankyou for using YoN book management service!")
                    break;
                else:
                    print("Enter the correct option")
                    continue;
            elif due>30:
                print("Fine amount for ",due,"days is : ",due*10)
                print("Your membership will be cancelled")
                pay=input("Are you willing to pay now (Y/N) : ")
                if pay=="Y" or pay=="y":
                    print("scan the QR code")
                    for i in range(8):
                        for j in range(20):
                            print("*",end="")
                        print("")
                    print("Now the book was added to the list")
                    print("Thankyou for using YoN book management service!")
                    break;
                elif pay=="N" or pay=="n":
                    returnday=input("when will you return the book?\n")
                    print("Return the book ASAP.....")
                    print("Thankyou for using YoN book management service!")
                    break;
                else:
                    print("Enter the correct option")
                    continue;
            else:
                print("Enter the correct value!")
                continue;
        else:
            print("\nYou have entered the wrong values so many times.")
            print("So the program has been terminated.....")
            self.books.append(receive_books)

books=["c","c++","java","python"]
a=libr(books)

msg= """
    1.Display book
    2.Borrow book
    3.Return book
    4.Exit
"""

while True:
    print(msg)
    ch=int(input("Enter ur choise : "))
    if ch==1:
        a.list_books()
    elif ch==2:
        book=input("Enter the book name : ")
        a.borrow_books(book)
    elif ch==3:
        book=input("Enter the book name : ")
        a.receive_books(book)
    elif ch==4:
        print("Thankyou!\nSee you again")
        break
    else:
        print("You have entered a wrong option")
        quit()