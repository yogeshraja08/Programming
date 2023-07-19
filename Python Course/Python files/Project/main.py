from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import database

db=database("D:/Documents/python course/database/database.db")

root = Tk()
root.title("YoN Employee Management System")
root.geometry("1280x720+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")    # opens at maximized screen
root.iconphoto(False,PhotoImage(file="D:/Documents/python course/projects/py.png"))

name = StringVar()
age = StringVar()
gender = StringVar()
email = StringVar()
doj = StringVar()
contact = StringVar()
address = StringVar()

# entries frame
entries_frame = Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title = Label(entries_frame,text="YoN Employee Management System",font=("calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=5,pady=10)

lblname = Label(entries_frame,text="Name",font=("calibri",16),bg="#535c68",fg="white")
lblname.grid(row=1,column=0,padx=5,pady=10,sticky="w")
txtname = Entry(entries_frame,textvariable=name,font=("calibri",16),width=30)
txtname.grid(row=1,column=1,padx=5,pady=10,sticky="w")

lblage = Label(entries_frame,text="Age",font=("calibri",16),bg="#535c68",fg="white")
lblage.grid(row=1,column=2,padx=5,pady=10,sticky="w")
txtage = Entry(entries_frame,textvariable=age,font=("calibri",16),width=30)
txtage.grid(row=1,column=3,padx=5,pady=10,sticky="w")

lbldoj = Label(entries_frame,text="D.O.J.",font=("calibri",16),bg="#535c68",fg="white")
lbldoj.grid(row=2,column=0,padx=5,pady=10,sticky="w")
txtdoj = Entry(entries_frame,textvariable=doj,font=("calibri",16),width=30)
txtdoj.grid(row=2,column=1,padx=5,pady=10,sticky="w")

lblgender = Label(entries_frame,text="Gender",font=("calibri",16),bg="#535c68",fg="white")
lblgender.grid(row=2,column=2,padx=5,pady=10,sticky="w")
txtgender = ttk.Combobox(entries_frame,font=("calibri",16),width=28,textvariable=gender,state="readonly")
txtgender['values'] = ("Male","Female","Trans-gender")
txtgender.grid(row=2,column=3,padx=5,pady=10,sticky="w")

lblemail = Label(entries_frame,text="Email",font=("calibri",16),bg="#535c68",fg="white")
lblemail.grid(row=3,column=0,padx=5,pady=10,sticky="w")
txtemail = Entry(entries_frame,textvariable=email,font=("calibri",16),width=30)
txtemail.grid(row=3,column=1,padx=5,pady=10,sticky="w")

lblcontact = Label(entries_frame,text="Contact",font=("calibri",16),bg="#535c68",fg="white")
lblcontact.grid(row=3,column=2,padx=5,pady=10,sticky="w")
txtcontact = Entry(entries_frame,textvariable=contact,font=("calibri",16),width=30)
txtcontact.grid(row=3,column=3,padx=5,pady=10,sticky="w")

lbladdress = Label(entries_frame,text="Address",font=("calibri",16),bg="#535c68",fg="white")
lbladdress.grid(row=4,column=0,padx=5,pady=0,sticky="w")
txtaddress = Text(entries_frame,font=("calibri",16),width=85,height=3)
txtaddress.grid(row=5,column=0,padx=5,pady=5,sticky="w",columnspan=4)


# button frame
def getdata(event):
    selected_row = result.focus()
    data_selected = result.item(selected_row)
    global row
    row = data_selected['values']
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[5])
    email.set(row[4])
    contact.set(row[6])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END, row[7])
    
def displayall():
    result.delete(*result.get_children())
    for row in db.fetch():
        result.insert("", END,values=row)
        
def add_emp():
    if txtname.get() == "" or txtage.get() == "" or txtgender.get() == "" or txtemail.get() == "" or txtdoj.get() == "" or txtcontact.get() == "" or txtaddress.get(1.0,END) == "" :
        messagebox.showerror("Error in Input","Please Fill All Details")
        return
    db.insert(txtname.get(), txtage.get(), txtdoj.get(), txtemail.get(), txtgender.get(), txtcontact.get(), txtaddress.get(1.0,END))
    messagebox.showinfo("Success","Record Inserted")
    clear_emp()
    displayall()

def edit_emp():
    if txtname.get() == "" or txtage.get() == "" or txtgender.get() == "" or txtemail.get() == "" or txtdoj.get() == "" or txtcontact.get() == "" or txtaddress.get(1.0,END) == "" :
        messagebox.showerror("Error in Input","Please Fill All Details")
        return
    db.update(row[0], txtname.get(), txtage.get(), txtdoj.get(), txtemail.get(), txtgender.get(), txtcontact.get(), txtaddress.get(1.0,END))
    messagebox.showinfo("Success","Record Updated")
    clear_emp()
    displayall()

def delete_emp():
    db.delete(row[0])
    clear_emp()
    displayall()

def clear_emp():
    name.set("")
    age.set("")
    gender.set("")
    email.set("")
    doj.set("")
    contact.set("")
    txtaddress.delete(1.0,END)


btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=5,pady=5,sticky="w")

add_btn = Button(btn_frame, command=add_emp,text="Add Details",width=15,font=("calibri",16),bg="#16a085",fg="white",bd=0)
add_btn.grid(row=0,column=0,padx=5,pady=5)

edit_btn = Button(btn_frame, command=edit_emp,text="Update Details",width=15,font=("calibri",16),bg="#16a085",fg="white",bd=0)
edit_btn.grid(row=0,column=1,padx=5,pady=5)

delete_btn = Button(btn_frame, command=delete_emp,text="Delete Details",width=15,font=("calibri",16),bg="#16a085",fg="white",bd=0)
delete_btn.grid(row=0,column=2,padx=5,pady=5)

clear_btn = Button(btn_frame, command=clear_emp,text="Clear Details",width=15,font=("calibri",16),bg="#16a085",fg="white",bd=0)
clear_btn.grid(row=0,column=3,padx=5,pady=5)


# table frames
table_frame = Frame(root,bg="white")
table_frame.place(x=0,y=397,width=1400,height=300)
style = ttk.Style()
style.configure("mystyle.Treeview",font=("calibri",16),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=("calibri",16))
result = ttk.Treeview(table_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")

result.heading("1", text="ID")
result.column("1", width=40)

result.heading("2", text="NAME")
#result.column("2", width=10)

result.heading("3", text="AGE")
result.column("3", width=40)

result.heading("4", text="D.O.J.")
result.column("4", width=100)

result.heading("5", text="EMAIL")
result.column("5", width=300)

result.heading("6", text="GENDER")
result.column("6", width=50)

result.heading("7", text="CONTACT")
result.column("7", width=100)

result.heading("8", text="ADDRESS")
#result.column("8", width=20)

result['show'] = 'headings'
result.bind("<ButtonRelease>",getdata)
result.pack(fill=X)

displayall()
root.mainloop()