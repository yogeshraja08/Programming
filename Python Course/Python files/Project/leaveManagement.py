import sqlite3
from tkinter import messagebox as tk
from tkinter.font import Font
from easygui import *
from tkinter import *
from turtle import *
import random

conn = sqlite3.connect("D:/Documents/python course/projects/database.db")
cur = conn.cursor()
conn.execute ('''CREATE TABLE if not exists balance (employee_id text,sickleave int,maternityleave int,emergencyleave int)''')
conn.execute('''CREATE TABLE if not exists status (leave_id int,employee_id text,leave text,Date1 text,Date2 text,days int,status text)''')
conn.execute('''CREATE TABLE if not exists employee (employee_id text,Name text,ContactNumber text,Password text)''')

def AdminLogin():
    message = "Enter Username and Password"
    title = "Admin Login"
    fieldnames = ["Username", "Password"]
    field = [multpasswordbox(message, title, fieldnames)]
    if field[0] == 'admin' and field[1] == 'admin':
        tk.showinfo("Admin Login", "Login Successfully")
        adminwindow()
    else:
        tk.showerror("Error info", "Incorrect username or password")

def EmployeeLogin():
    message = "Enter Employee ID and Password"
    title = "Employee Login"
    fieldnames = ["Employee ID", "Password"]
    field = [multpasswordbox(message, title, fieldnames)]
    f = 1
    for row in conn.execute('SELECT * FROM employee'):
        if field[0] == row[0] and field[1] == row[3]:
            global login
            login = field[0]
            print("Success")
            tk.showinfo("Employee Login", "Login Successfully")
            EmployeeLoginWindow()
        break
    if not f:
        print("Invalid")
        tk.showerror("Error info", "Incorrect employee id or password")


def Employeelogout():
    global login
    login = -1
    LoginWindow.destroy()

def EmployeeLeaveStatus():
    global leaveStatus
    leaveStatus = []
    for i in conn.execute('SELECT * FROM status where employee_id=?', login):
        leaveStatus = i
    WindowStatus()

def EmployeeAllStatus():
    allStatus = Toplevel()
    txt = Text(allStatus)
    for i in conn.execute('SELECT * FROM status where employee_id=?', login):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')
        txt.pack()

def EmployeeInformationWindow():
    employeeInformation = Toplevel()
    txt = Text(employeeInformation)
    for i in conn.execute('SELECT employee_id,Name,ContactNumber FROM employee where employee_id=?', login):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')
        txt.pack()
        
def EmployeeAllInformationWindow(): 
    allEmployeeInformation = Toplevel() 
    txt = Text(allEmployeeInformation)
    for i in conn.execute('SELECT employee_id,Name,ContactNumber FROM employee'):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')
        txt.pack()

def WindowStatus():
    StatusWindow = Toplevel()
    label_1 = Label(StatusWindow, text="Employee ID=", fg="blue", justify=LEFT, font=("Calibri", 16))
    label_2 = Label(StatusWindow, text=leaveStatus[1], font=("Calibri", 16))
    label_3 = Label(StatusWindow, text="Type=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_4 = Label(StatusWindow, text=leaveStatus[2], font=("Calibri", 16))
    label_5 = Label(StatusWindow, text="start=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_6 = Label(StatusWindow, text=leaveStatus[3], font=("Calibri", 16))
    label_7 = Label(StatusWindow, text="end=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_8 = Label(StatusWindow, text=leaveStatus[4], font=("Calibri", 16))
    label_9 = Label(StatusWindow, text="Status:", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_10 = Label(StatusWindow, text=leaveStatus[6], font=("Calibri", 16))
    label_11 = Label(StatusWindow, text="leave_id:", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_12 = Label(StatusWindow, text=leaveStatus[0], font=("Calibri", 16))
    label_1.grid(row=1, column=0)
    label_2.grid(row=1, column=1)
    label_3.grid(row=2, column=0)
    label_4.grid(row=2, column=1)
    label_5.grid(row=3, column=0)
    label_6.grid(row=3, column=1)
    label_7.grid(row=4, column=0)
    label_8.grid(row=4, column=1)
    label_9.grid(row=5, column=0)
    label_10.grid(row=5, column=1)
    label_11. grid(row=0, column=0)
    label_12.grid(row=0, column=1)

def balance():
    global login
    check = (login,)
    global balanced
    balanced = []
    for i in conn.execute('SELECT * FROM balance WHERE employee_id = ?', check):
        balanced = i
        WindowBalance()

def WindowBalance():
    balanceWindow = Toplevel()
    label_1 = Label(balanceWindow, text="Employee ID=", fg="blue", justify=LEFT, font=("Calibri", 16))
    label_2 = Label(balanceWindow, text=balanced[0], font=("Calibri", 16))
    label_3 = Label(balanceWindow, text="Sick Leave=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_4 = Label(balanceWindow, text=balanced[1], font=("Calibri", 16))
    label_5 = Label(balanceWindow, text="Maternity Leave=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_6 = Label(balanceWindow, text=balanced[2], font=("Calibri", 16))
    label_7 = Label(balanceWindow, text="Emergency Leave=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_8 = Label(balanceWindow, text=balanced[3], font=("Calibri", 16))
    label_1.grid(row=0, column=0)
    label_2.grid(row=0, column=1)
    label_3.grid(row=1, column=0)
    label_4.grid(row=1, column=1)
    label_5.grid(row=2, column=0)
    label_6.grid(row=2, column=1)
    label_7.grid(row=3, column=0)
    label_8.grid(row=3, column=1)

def apply():
    message = "Enter the following details "
    title = "Leave Apply"
    fieldNames = ["Employee ID", "From", "To", "days"] 
    fieldValues = [multenterbox(message, title, fieldNames)]
    message1 = "Select type of leave"
    title1 = "Type of leave"
    choices = ["Sick leave", "Maternity leave", "Emergency leave"]
    choice = choicebox(message1, title1, choices)
    leaveid = random.randint(1, 1000)
    conn.execute("INSERT INTO status(leave_id,employee_id,leave,Date1,Date2,days,status) VALUES (?,?,?,?,?,?,?)",(leaveid, fieldValues[0], choice, fieldValues[1], fieldValues[2], fieldValues[3], "Pending"))
    conn.commit()

def LeaveApproval():
    message = "Enter leave_id"
    title = "leave approval"
    fieldNames = ["Leave_id"]
    fieldValues = [multenterbox(message, title, fieldNames)]
    message1 = "Approve/Deny"
    title1 = "leave approval"
    choices = ["approve", "deny"]
    choice = choicebox(message1, title1, choices)
    conn.execute("UPDATE status SET status = ? WHERE leave_id= ?", (choice, fieldValues[0]))
    conn.commit()
    if choice == 'approve':
        print(0)
        cur.execute("SELECT leave FROM status WHERE leave_id=?", (fieldValues[0],))
        row = cur.fetchall()
        col = row
        for row in conn.execute("SELECT employee_id FROM status WHERE leave_id=?", (fieldValues[0],)):
            print(2)
        exampleId = row[0]
        for row in conn.execute("SELECT days FROM status WHERE leave_id=?", (fieldValues[0],)):
            print(2)
        exampleDays = row[0]
        balance = row[0]
        for row in conn.execute("SELECT sickleave from balance where employee_id=?", (exampleId,)):
            print(balance)
        balance1 = row[0]
        for row in conn.execute("SELECT maternityleave from balance where employee_id=?", (exampleId,)):
            print(balance1)
        balance2 = row[0]
        for row in conn.execute("SELECT emergencyleave from balance where employee_id=?", (exampleId,)):
            print(balance2)
        if (col[0] == ('sickleave',)):
            print(3)
            conn.execute("UPDATE balance SET sickleave =? WHERE employee_id= ?", ((balance - exampleDays), (exampleId)))
        if (col[0] == ('maternityleave',)):
            print(3)
            conn.execute("UPDATE balance SET maternityleave =? WHERE employee_id= ?", ((balance1 - exampleDays), (exampleId)))
        if (col[0] == ('emergencyleave',)):
            print(3)
            conn.execute("UPDATE balance SET emergencyleave =? WHERE employee_id= ?", ((balance2 - exampleDays), (exampleId)))

def leavelist():
    leavelistwindow = Toplevel()
    txt = Text(leavelistwindow)
    for i in conn.execute('SELECT * FROM status'):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')
        txt.pack()
        
def registration():
        message = "Enter Details of Employee"
        title = "Registration"
        fieldNames = ["Employee ID", "Name", "Contact Number", "Password"]
        fieldValues = [multpasswordbox(message, title, fieldNames)]
        while 1 :
            errmsg = ""
            if fieldValues == None: 
                for i in range(len(fieldNames)):
                    if fieldValues[i].strip() == "":
                        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
                break


            if errmsg == "":
                fieldValues = [multpasswordbox(errmsg, title, fieldNames, fieldValues)]
                conn.execute("INSERT INTO employee(employee_id,Name,ContactNumber,Password) VALUES (?,?,?,?)",(fieldValues[0], fieldValues[1], fieldValues[2], fieldValues[3]))
                conn.execute("INSERT INTO balance(employee_id,sickleave,maternityleave,emergencyleave) VALUES (?,?,?,?)", (fieldValues[0], 12, 12, 50))
                conn.commit()
                break


def EmployeeLoginWindow():
    global LoginWindow
    LoginWindow = Toplevel()
    LoginWindow.wm_attributes('-fullscreen', '1')
    BtnFont = Font(family='Calibri(Body)', size=20)
    filename = PhotoImage(file="D:\Documents\python course\projects\py.png")
    Background_Label = Label(LoginWindow, image=filename)
    Background_Label.place(x=0, y=0, relwidth=1, relheight=1)
    informationEmployee = Button(LoginWindow, text='Employee information', command=EmployeeInformationWindow, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3", font=("Calibri", 36, "bold"), pady=3)
    informationEmployee['font'] = BtnFont
    informationEmployee.pack(fill=X)
    submit = Button(LoginWindow, text='Submit Leave', command=apply, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3", font=("Calibri", 36, "bold"), pady=3)
    submit['font'] = BtnFont
    submit.pack(fill=X)
    LeaveBalance = Button(LoginWindow, text='Leave Balance', command=balance, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3", font=("Calibri", 36, "bold"), pady=3)
    LeaveBalance['font'] = BtnFont
    LeaveBalance.pack(fill=X)
    LeaveApplicationStatus = Button(LoginWindow, text='Last leave status', command=EmployeeLeaveStatus, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3", font=("Calibri", 36, "bold"), pady=3)
    LeaveApplicationStatus['font'] = BtnFont
    LeaveApplicationStatus.pack(fill=X)
    AllLeaveStatus	=	Button(LoginWindow,	text='All	leave	status',
    command=EmployeeAllStatus, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3", font=("Calibri", 36, "bold"), pady=3)
    AllLeaveStatus['font'] = BtnFont
    AllLeaveStatus.pack(fill=X)
    LogoutBtn = Button(LoginWindow, text='Logout', bd=12, relief=GROOVE, fg="red", bg="#ffffb3", font=("Calibri", 36, "bold"), pady=3, command=Employeelogout)
    LogoutBtn['font'] = BtnFont
    LogoutBtn.pack(fill=X)
    informationEmployee.pack()
    submit.pack()
    LeaveBalance.pack()
    LeaveApplicationStatus.pack()
    AllLeaveStatus.pack()
    LogoutBtn.pack()

def adminwindow():
    adminmainwindow = Toplevel()
    adminmainwindow.wm_attributes('-fullscreen', '1')
    Background_Label = Label(adminmainwindow, image=filename)
    Background_Label.place(x=0, y=0, relwidth=1, relheight=1)
    informationEmployee	=	Button(adminmainwindow,	text='All	Employee information', command=EmployeeAllInformationWindow, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3", font=("Calibri", 36, "bold"), pady=3)
    informationEmployee['font'] = BtnFont
    informationEmployee.pack(fill=X)
    LeaveListButton = Button(adminmainwindow, text='Leave approval list', command=leavelist, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",font=("Calibri", 36, "bold"), pady=3)
    LeaveListButton['font'] = BtnFont
    LeaveListButton.pack(fill=X)
    ApprovalButton = Button(adminmainwindow, text='Approve leave', command=LeaveApproval, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",font=("Calibri", 36, "bold"), pady=3) 
    ApprovalButton['font'] = BtnFont 
    ApprovalButton.pack(fill=X)
    LogoutBtn = Button(adminmainwindow, text='Logout', command=adminmainwindow.destroy, bd=12, relief=GROOVE, fg="red",bg="#ffffb3",font=("Calibri", 36, "bold"), pady=3)
    LogoutBtn['font'] = BtnFont
    LogoutBtn.pack(fill=X)
    informationEmployee.pack()
    LeaveListButton.pack()
    ApprovalButton.pack()
    
root = Tk()
root.wm_attributes('-fullscreen', '1')
root.title("Leave Management System")
root.iconbitmap(default="D:\Documents\python course\projects\py.png")
filename = PhotoImage(file="D:\Documents\python course\projects\py.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
MainLabel = Label(root, text="Leave Management System", bd=12, relief=GROOVE, fg="White", bg="blue", font=("Calibri", 36, "bold"), pady=3)
MainLabel.pack(fill=X)
im = PhotoImage(file="D:\Documents\python course\projects\py.png")
AdminLgnBtn = Button(root, text='Admin login', bd=12, relief=GROOVE, fg="blue", bg="#ffffb3", font=("Calibri", 36, "bold"), pady=3, command=AdminLogin)
BtnFont = Font(family='Calibri(Body)', size=20)
AdminLgnBtn['font'] = BtnFont
AdminLgnBtn.pack(fill=X)
LoginBtn = Button(root, text='Employee login', bd=12, relief=GROOVE, fg="blue", bg="#ffffb3", font=("Calibri", 36, "bold"), pady=3, command=EmployeeLogin)
LoginBtn['font'] = BtnFont
LoginBtn.pack(fill=X)
EmployeeRegistration = Button(root, text='Employee registration', command=registration, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3", font=("Calibri", 36, "bold"), pady=3)
EmployeeRegistration['font'] = BtnFont
EmployeeRegistration.pack(fill=X)
ExitBtn = Button(root, text='Exit', command=root.destroy, bd=12, relief=GROOVE, fg="red", bg="#ffffb3", font=("Calibri", 36, "bold"), pady=3)
ExitBtn['font'] = BtnFont
ExitBtn.pack(fill=X)
ExitBtn.pack()
MainLabel.pack()
AdminLgnBtn.pack()
LoginBtn.pack()
EmployeeRegistration.pack()
root.mainloop()