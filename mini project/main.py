# Importing modules
from logging import root
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as tkm, messagebox
import mysql.connector as mysc
import tkinter.font as tkfont
import sqlite3

# ======================DATABASE===================================

global mydb
global mycurr
myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03", database ='miniproject',auth_plugin='mysql_native_password')


# creating database for  creating employee table
def createdb():
    p1 = passw1.get()
    p2 = passw2.get()
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    if p1 == p2:
        mycurr = myconn.cursor()
        mycurr.execute("use project")
        create = "CREATE TABLE if not exists employee(s_no integer primary key auto_increment,Fname varchar(20),user_name varchar(20) ,email_id varchar(50),phonenumber varchar(15),experiences varchar(3),password varchar(20) default '123456789')"
        mycurr.execute(create)
        myconn.commit()
        db()
        mycurr.close()
    else:
        tkm.showerror("Matching", "Password and confirm password doesn't match")

    fullname.set('')
    username.set('')
    eid.set('')
    phonenum.set('')
    passw1.set('')
    passw2.set('')


# creating database for  creating employee table
def createdbadd():
    FIRSTNAME.set('')
    USERNAME.set('')
    AGE.set('')
    EADDRESS.set('')
    CONTACT.set('')
    EXPERIENCE.set('')
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    mycurr = myconn.cursor()
    mycurr.execute("use project")
    create = "CREATE TABLE if not exists employee(s_no integer primary key auto_increment,Fname varchar(20),user_name varchar(20) ,email_id varchar(50),phonenumber varchar(15),experiences varchar(3),password varchar(20) default '123456789')"
    mycurr.execute(create)
    myconn.commit()
    dbadd()
    mycurr.close()


# creating database for  creating employee table
def createdbup():
    UPDATENAME.set('')
    NEWNAME.set('')
    NEWUSERNAME.set('')
    NEWID.set('')
    NEWPHONE.set('')
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    mycurr2 = myconn.cursor()
    mycurr2.execute("use project")
    create2 = "CREATE TABLE if not exists employee(s_no integer primary key auto_increment,Fname varchar(20),user_name varchar(20) ,email_id varchar(50),phonenumber varchar(15),experiences varchar(3),password varchar(20) default '123456789')"
    mycurr2.execute(create2)
    myconn.commit()
    dbupdate()
    mycurr2.close()


# creating database for  creating feedback table

def createfeed():
    FEEDMAIL.set('')
    FEEDQUERY.set('')
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")

    mycurr4 = myconn.cursor()
    mycurr4.execute("use project")
    create4 = "CREATE TABLE if not exists feedback(emailid varchar(30),query varchar(256))"
    mycurr4.execute(create4)
    myconn.commit()
    dbfeed()
    mycurr4.close()


# creating database for  creating vacancy table
def createdbvacancy():
    COMPANY.set('')
    INDUSTRY.set('')
    ROLE.set('')
    PLACE.set('')
    FIELD.set('')
    EXPER.set('')
    SKILL.set('')
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    mycurr1 = myconn.cursor()
    mycurr1.execute("use project")
    create1 = "CREATE TABLE if not exists vacancy(S_no integer auto_increment primary key,Company varchar(50),Role varchar(40),Industry varchar(30),Place varchar(25),field varchar(40),experiences varchar(3),Skills varchar(50))"
    mycurr1.execute(create1)
    myconn.commit()
    dbvacancy()
    mycurr1.close()


# =====================DATABASE FUNCTIONS===================================

# updating employee table
def dbupdate():
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    mycurr = myconn.cursor()
    mycurr.execute("use project")
    que = "UPDATE employee set Fname=%s,user_name=%s,email_id=%s,phonenumber=%s WHERE Fname=%s"
    val = (NEWNAME.get(), NEWUSERNAME.get(), NEWID.get(), NEWPHONE.get(), UPDATENAME.get())
    mycurr.execute(que, val)
    myconn.commit()
    mycurr.close()
    tkm.showinfo("Update", "Updated Employee details successful!!")


# inserting values entered from user side in employee table
def dbfeed():
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    mycurr = myconn.cursor()
    mycurr.execute("use project")
    sql = "INSERT INTO feedback(emailid,query) VALUES (%s,%s)"
    val = (FEEDMAIL.get(), FEEDQUERY.get())
    mycurr.execute(sql, val)
    myconn.commit()
    tkm.showinfo("Feedback", "feedback Submitted.")


# inserting values entered from user side in employee table
def dbadd():
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    mycurr = myconn.cursor()
    mycurr.execute("use project")
    sql = "INSERT INTO employee(Fname,user_name,email_id,phonenumber,experiences) VALUES (%s,%s,%s,%s,%s)"
    val = (FIRSTNAME.get(), USERNAME.get(), EADDRESS.get(), CONTACT.get(), EXPERIENCE.get())
    mycurr.execute(sql, val)
    myconn.commit()
    tkm.showinfo("Adding", "Add Employee successful!!")


# inserting values entered from user side in vacancy table
def dbvacancy():
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    mycurr = myconn.cursor()
    mycurr.execute("use project")
    sql = "INSERT INTO vacancy(Company,Industry,Role,Place,field,experiences,skills) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (COMPANY.get(), INDUSTRY.get(), ROLE.get(), PLACE.get(), FIELD.get(), EXPER.get(), SKILL.get())
    mycurr.execute(sql, val)
    myconn.commit()
    tkm.showinfo("Vacancy", "Added Vacancy")


# inserting values entered from user side in employee table
def db():
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    mycurr = myconn.cursor()
    mycurr.execute("use project")
    sql = "INSERT INTO employee(Fname,user_name,email_id,phonenumber,password) VALUES (%s,%s,%s,%s,%s)"
    val = (fullname.get(), username.get(), eid.get(), phonenum.get(), passw1.get())
    mycurr.execute(sql, val)
    myconn.commit()


# =====================FUNCTIONS===================================
# checking for username and password if it is correct or not
def check(u, p):
    if u == 'admin' and p == '12345':
        admin()
    else:
        tkm.showerror("Invalid", "Incorrect Username/password")


# login page for admin where admin enters his username and password
def login_admin():
    root4 = Tk()
    root4.title("LOGIN DETAILS")
    root4.geometry('600x500+450+150')
    root4.configure(bg="grey")

    # fa=Frame(root4)
    # fa.place(x=0,y=0)
    # img5=ImageTk.PhotoImage(Image.open("Projectimages/adminimg.jpg"))
    # lb3=Label(root4,image=img5)
    # lb3.image=img5
    # lb3.place(x=0,y=0,relwidth=1,relheight=1)

    lt = Label(root4, text="LOGIN HERE", font=('arial', 20), bg="light grey")
    lt.place(x=200, y=20)
    l1 = Label(root4, text="Username ", bg="light grey", font=('arial', 14))
    l1.place(x=50, y=90)
    e1 = Entry(root4, width=25, font=('arial', 14), textvariable=usernameL)
    e1.place(x=170, y=90)

    l2 = Label(root4, text="Password ", bg="light grey", font=('arial', 14))
    l2.place(x=50, y=120)
    e2 = Entry(root4, width=25, show="*", font=('arial', 14), textvariable=passwordL)
    e2.place(x=170, y=120)
    b1 = Button(root4, text="Login", font=('arial', 15), width=6, height=1, command=lambda: check(e1.get(), e2.get()))
    b1.place(x=240, y=170)
    root4.mainloop()


# employee chooses his type whether he is new employee or existing employee
def login_employee():
    root5 = Tk()
    root5.geometry('500x400+500+150')
    b3 = Button(root5, text="New User", command=register)
    b3.place(x=130, y=200)
    b4 = Button(root5, text="Existing User", command=login)
    b4.place(x=270, y=200)
    root5.mainloop()


# If employee is new then he register himself in this company
def register():
    rootv = Tk()
    rootv.geometry("700x400+450+200")
    # ===================LABELS==============================
    lbl_title = Label(rootv, text="Enter your details ", font=('arial', 16), bg="yellow", width=30)
    lbl_title.grid(row=0, column=0, columnspan=2)
    lbl_comp = Label(rootv, text="Full Name", font=('arial', 14), bd=5)
    lbl_comp.grid(row=2, sticky=W)
    lbl_indus = Label(rootv, text="Username", font=('arial', 14), bd=5)
    lbl_indus.grid(row=3, sticky=W)
    lbl_role = Label(rootv, text="Email Id", font=('arial', 14), bd=5)
    lbl_role.grid(row=4, sticky=W)
    lbl_skill = Label(rootv, text="Phone Number", font=('arial', 14), bd=5)
    lbl_skill.grid(row=5, sticky=W)
    lbl_field = Label(rootv, text="password", font=('arial', 14), bd=5)
    lbl_field.grid(row=6, sticky=W)
    lbl_exper = Label(rootv, text="Confirm password", font=('arial', 14), bd=5)
    lbl_exper.grid(row=7, sticky=W)
    # ===================ENTRY===============================
    comp = Entry(rootv, width=20, textvariable=Fname, font=('arial', 14))
    comp.grid(row=2, column=1)
    indus = Entry(rootv, width=20, textvariable=Uname, font=('arial', 14))
    indus.grid(row=3, column=1)
    role = Entry(rootv, width=20, textvariable=eid, font=('arial', 14))
    role.grid(row=4, column=1)
    place = Entry(rootv, width=20, textvariable=phn, font=('arial', 14))
    place.grid(row=5, column=1)
    field = Entry(rootv, width=20, textvariable=pswd, font=('arial', 14))
    field.grid(row=6, column=1)
    exper = Entry(rootv, width=20, textvariable=cpswd, font=('arial', 14))
    exper.grid(row=7, column=1)
    badd = Button(rootv, text="Register", command=Submitrr, font=('arial', 14), width=20)
    badd.grid(row=9, column=1)
    rootv.mainloop()


# If employee is new then he register himself in this company
def register():
    root6 = Tk()
    root6.geometry('500x400+500+150')

    llfont = tkfont.Font(family="Helvetica", size=20, weight=tkfont.BOLD)
    ll = Label(root6, text="Enter your details ", font=llfont)
    ll.grid(row=0, column=0, columnspan=2)

    l6 = Label(root6, text="Full Name :")
    l6.grid(row=2, sticky=W)
    e3 = Entry(root6, width=30, textvariable=fullname)
    e3.grid(row=2, column=1)

    l7 = Label(root6, text="Username :")
    l7.grid(row=3, sticky=W)
    e4 = Entry(root6, width=30, textvariable=username)
    e4.grid(row=3, column=1)

    l8 = Label(root6, text="Email Id :")
    l8.grid(row=4, sticky=W)
    e5 = Entry(root6, width=30, textvariable=eid)
    e5.grid(row=4, column=1)

    l9 = Label(root6, text="Phone Number :")
    l9.grid(row=5, sticky=W)
    e6 = Entry(root6, width=30, textvariable=phonenum)
    e6.grid(row=5, column=1)

    l10 = Label(root6, text="password :")
    l10.grid(row=6, sticky=W)
    e7 = Entry(root6, width=30, show="*", textvariable=passw1)
    e7.grid(row=6, column=1)

    l11 = Label(root6, text="Confirm password :")
    l11.grid(row=7, sticky=W)
    e8 = Entry(root6, width=30, show="*", textvariable=passw2)
    e8.grid(row=7, column=1)

    bsub = Button(root6, text="   REGISTER   ", command=createdb)
    bsub.grid(row=8, column=1)

    root6.mainloop()


# If employee is existing user then he will login through his credentials
def existing_user():
    root7 = Tk()
    root7.title("LOGIN DETAILS")
    root7.geometry('500x400+500+150')
    global e1
    global e2
    lt1 = Label(root7, text="LOGIN", font=('arial', 14))
    lt1.grid(row=0, column=0, columnspan=3)
    lu = Label(root7, text="Username :")
    lu.grid(row=2, sticky=W)
    e1 = Entry(root7, width=35, textvariable=usernameE)
    e1.grid(row=2, column=1)

    lp = Label(root7, text="Password :")
    lp.grid(row=3, sticky=W)
    e2 = Entry(root7, width=35, show="*", textvariable=passwordE)
    e2.grid(row=3, column=1)
    bl = Button(root7, text="     Login    ", command=verify_user)
    bl.place(x=210, y=120)
    root7.mainloop()


# checking for employee credentials with the saved database whether it is correct or not
def verify_user():
    usernameE.set('')
    passwordE.set('')
    username1 = usernameE.get()
    passwrd1 = passwordE.get()
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    mycurr = myconn.cursor()
    mycurr.execute("use project")
    que = "SELECT password FROM employee WHERE user_name = %s"
    val = (username1,)
    mycurr.execute(que, val)
    checking = mycurr.fetchone()
    if passwrd1 == checking[0]:
        employee()
    else:
        tkm.showerror("Invalid", "Incorrect Username/password")


# employee views vacancy which are uploaded by administrator
def viewV():
    rootva = Tk()
    rootva.geometry('1200x500+150+250')
    rootva.configure(bg="light grey")
    rootva.title("EMPLOYEES")
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    mycurr = myconn.cursor()
    mycurr.execute("use project")
    create = "select * from vacancy"
    mycurr.execute(create)
    records = mycurr.fetchall()
    print_records = ""
    for record in records:
        for i in record:
            print_records += str(i) + " "
        print_records += '\n'

    lt = Label(rootva, text="Vacancies")
    lt.place(x=100, y=40)
    lh = Label(rootva, text="s.no\tCompany\trole\tindustry\tplace\tfield\texperiences\tskills", font=('arial', 14),
               bg="black", fg="white")
    lh.place(x=100, y=75)

    ld = Label(rootva, text=print_records, font=('arial', 16), bg="grey")
    ld.place(x=100, y=100)
    myconn.commit()
    mycurr.close()
    rootva.mainloop()


# administrator view all the employee details who are there
def viewC():
    rootvi = Tk()
    rootvi.geometry('800x500+150+250')
    rootvi.configure(bg="light grey")
    rootvi.title("EMPLOYEES")
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    mycurr = myconn.cursor()
    mycurr.execute("use project")
    create = "select * from employee"
    mycurr.execute(create)
    records = mycurr.fetchall()
    print_records = ""
    for record in records:
        for i in record:
            print_records += str(i) + '\t'
        print_records += '\n'

    lt = Label(rootvi, text="Employees")
    lt.place(x=100, y=40)
    lh = Label(rootvi, text="s.no\tFullname\tUsername\t Email_ID\tPhoneNumber\tExperiences\tPassword(default)",
               font=('arial', 14), bg="black", fg="white", width=60)
    lh.place(x=100, y=75)

    ld = Label(rootvi, text=print_records, font=('arial', 16), bg="grey")
    ld.place(x=100, y=100)
    myconn.commit()
    mycurr.close()
    rootvi.mainloop()


# admin view all the feedback that are given by employee
def viewfeed():
    root3 = Tk()
    root3.geometry('700x600+100+100')
    root3.title("FEEDBACK")
    myconn = mysc.connect(host="localhost", user="root", passwd="Tanvi@03")
    mycurr = myconn.cursor()
    mycurr.execute("use project")
    create = "select * from feedback"
    mycurr.execute(create)
    records = mycurr.fetchall()
    print_records = ""
    for record in records:
        for i in record:
            print_records += str(i) + '\t'
        print_records += '\n'

    lv = Label(root3, text="Feedback", font=('arial', 20))
    lv.place(x=130, y=40)
    lh = Label(root3, text="emailid\tquery", font=('arial', 14), bg="black", fg="white", width=60)
    lh.place(x=100, y=75)
    ld = Label(root3, text=print_records, font=('arial', 16), bg="grey")
    ld.place(x=100, y=100)
    root3.mainloop()


# employee asks help for administration
def askH():
    roota = Tk()
    roota.geometry('800x600+100+100')
    ll = Label(roota, text="Ask Your Query", font=('arial', 30))
    ll.grid(row=0, column=4)

    le = Label(roota, text="Your email id :", font=('arial', 14))
    le.grid(row=4, column=3)
    lf = Label(roota, text="Your query :", font=('arial', 14))
    lf.grid(row=5, column=3)

    ee = Entry(roota, textvariable=FEEDMAIL, width=30, font=('arial', 10))
    ee.grid(row=4, column=4, columnspan=2)
    ef = Entry(roota, textvariable=FEEDQUERY, width=30, font=('arial', 10))
    ef.grid(row=5, column=4, rowspan=3, columnspan=2, padx=10, pady=10, ipady=10)
    bs = Button(roota, text="Submit", command=createfeed)
    bs.grid(row=9, column=4)
    roota.mainloop()


# employee logs feedback
def logfeedback():
    rootf = Tk()
    rootf.geometry('800x600+100+100')
    img6 = ImageTk.PhotoImage(Image.open("pink-flamingo-design-plain.jpg"))
    lba = Label(rootf, image=img6)
    lba.image = img6
    lba.place(x=0, y=0, relwidth=1, relheight=1)
    ll = Label(rootf, text="Give Feedback", font=('arial', 30))
    ll.grid(row=0, column=4)

    le = Label(rootf, text="Your email id :", font=('arial', 14))
    le.grid(row=4, column=3)
    lf = Label(rootf, text="Write your feedback :", font=('arial', 14))
    lf.grid(row=5, column=3)

    ee = Entry(rootf, textvariable=FEEDMAIL, width=30, font=('arial', 10))
    ee.grid(row=4, column=4, columnspan=2)
    ef = Entry(rootf, textvariable=FEEDQUERY, width=30, font=('arial', 10))
    ef.grid(row=5, column=4, rowspan=3, columnspan=2, padx=10, pady=10, ipady=10)
    bs = Button(rootf, text="Submit", command=createfeed)
    bs.grid(row=9, column=4)
    rootf.mainloop()


# if admin press exit then it prompts admin for log out
def aexit(root):
    iexit = tkm.askyesno("Log Out", "Do you want to Log Out ?")
    if iexit > 0:
        root.destroy()
        return


# admin adds vacancy for employee
def addV():
    rootv = Toplevel()
    rootv.geometry("500x400+250+150")

    img5 = ImageTk.PhotoImage(Image.open("977c2e8c480428e79cc15cdffdda95ad.jpg"))
    lb3 = Label(rootv, image=img5)
    lb3.image = img5
    lb3.place(x=0, y=0, relwidth=1, relheight=1)
    # ===================LABELS==============================
    lbl_title = Label(rootv, text="ADD VACANCY", font=('arial', 16), bg="light green", width=30)
    lbl_title.grid(row=0, column=0, columnspan=2)
    lbl_comp = Label(rootv, text="Company", font=('arial', 14),bg="light green", bd=5)
    lbl_comp.grid(row=2, sticky=W)
    lbl_indus = Label(rootv, text="Industry", font=('arial', 14),bg="light green", bd=5)
    lbl_indus.grid(row=3, sticky=W)
    lbl_role = Label(rootv, text="Role", font=('arial', 14),bg="light green", bd=5)
    lbl_role.grid(row=4, sticky=W)
    lbl_skill = Label(rootv, text="Place", font=('arial', 14),bg="light green", bd=5)
    lbl_skill.grid(row=5, sticky=W)
    lbl_field = Label(rootv, text="Field", font=('arial', 14),bg="light green", bd=5)
    lbl_field.grid(row=6, sticky=W)
    lbl_exper = Label(rootv, text="Experiences", font=('arial', 14),bg="light green", bd=5)
    lbl_exper.grid(row=7, sticky=W)
    lbl_skill = Label(rootv, text="Skills Required", font=('arial', 14),bg="light green", bd=5)
    lbl_skill.grid(row=8, sticky=W)
    # ===================ENTRY===============================
    comp = Entry(rootv, width=20, textvariable=COMPANY, font=('arial', 14))
    comp.grid(row=2, column=1)
    indus = Entry(rootv, width=20, textvariable=INDUSTRY, font=('arial', 14))
    indus.grid(row=3, column=1)
    role = Entry(rootv, width=20, textvariable=ROLE, font=('arial', 14))
    role.grid(row=4, column=1)
    place = Entry(rootv, width=20, textvariable=PLACE, font=('arial', 14))
    place.grid(row=5, column=1)
    field = Entry(rootv, width=20, textvariable=FIELD, font=('arial', 14))
    field.grid(row=6, column=1)
    exper = Entry(rootv, width=20, textvariable=EXPER, font=('arial', 14))
    exper.grid(row=7, column=1)
    skill = Entry(rootv, width=20, textvariable=SKILL, font=('arial', 14))
    skill.grid(row=8, column=1)
    badd = Button(rootv, text="+Add vacancy", command=createdbvacancy, font=('arial', 14), width=20)
    badd.grid(row=9, column=1)
    rootv.mainloop()


# admin updates employee details
def updateC():
    rootup = Tk()
    rootup.title("UPDATE DETAILS")
    rootup.geometry("500x400+450+150")

    img5 = ImageTk.PhotoImage(Image.open("977c2e8c480428e79cc15cdffdda95ad.jpg"))
    lb3 = Label(rootup, image=img5)
    lb3.image = img5
    lb3.place(x=0, y=0, relwidth=1, relheight=1)

    lbl_title = Label(rootup, text="Update Details", font=('arial', 16), bg="blue", width=30)
    lbl_title.grid(row=0, column=0, columnspan=2)
    lbl_firstname = Label(rootup, text="Update for", font=('arial', 14), bg="blue",bd=5)
    lbl_firstname.grid(row=2, sticky=W)
    lbl_lastname = Label(rootup, text="New Name", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=3, sticky=W)
    lbl_gender = Label(rootup, text="New Username", font=('arial', 14), bd=5)
    lbl_gender.grid(row=4, sticky=W)
    lbl_age = Label(rootup, text="New Email Id", font=('arial', 14), bd=5)
    lbl_age.grid(row=5, sticky=W)
    lbl_address = Label(rootup, text="New phone number", font=('arial', 14), bd=5)
    lbl_address.grid(row=6, sticky=W)

    # ===================ENTRY===============================
    firstname = Entry(rootup, width=20, textvariable=UPDATENAME, font=('arial', 14))
    firstname.grid(row=2, column=1)
    newname = Entry(rootup, width=20, textvariable=NEWNAME, font=('arial', 14))
    newname.grid(row=3, column=1)
    newuser = Entry(rootup, width=20, textvariable=NEWUSERNAME, font=('arial', 14))
    newuser.grid(row=4, column=1)
    address = Entry(rootup, width=20, textvariable=NEWID, font=('arial', 14))
    address.grid(row=5, column=1)
    contact = Entry(rootup, width=20, textvariable=NEWPHONE, font=('arial', 14))
    contact.grid(row=6, column=1)

    bu = Button(rootup, text="Update", command=createdbup, font=('arial', 14), width=20)
    bu.grid(row=7, column=1)

    rootup.mainloop()


# admin adds employee details
def addM():
    addform = Toplevel()
    width = 500
    height = 400
    addform.geometry("%dx%d+%d+%d" % (width, height, 80, 80))
    if "NewWindow" in globals():
        NewWindow.destroy()

    img6 = ImageTk.PhotoImage(Image.open("977c2e8c480428e79cc15cdffdda95ad.jpg"))
    lb3 = Label(addform, image=img6)
    lb3.image = img6
    lb3.place(x=0, y=0, relwidth=1, relheight=1)
    # ===================FRAMES==============================
    FormTitle = Frame(addform)
    FormTitle.grid(row=0, column=0, columnspan=2)
    ContactForm = Frame(addform)
    ContactForm.grid(row=0, column=0, columnspan=2)
    RadioGroup = Frame(addform)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male", font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female", font=('arial', 14)).pack(side=LEFT)

    # ===================LABELS==============================
    lbl_title = Label(addform, text="ADD EMPLOYEE DETAILS", font=('arial', 16), bg="orange", width=30)
    lbl_title.grid(row=0, column=0, columnspan=2)
    lbl_firstname = Label(addform, text="Fullname", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=2, sticky=W)
    lbl_lastname = Label(addform, text="Username", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=3, sticky=W)
    lbl_gender = Label(addform, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=4, sticky=W)
    lbl_age = Label(addform, text="Age", font=('arial', 14), bd=5)
    lbl_age.grid(row=5, sticky=W)
    lbl_address = Label(addform, text="E-mail Address", font=('arial', 14), bd=5)
    lbl_address.grid(row=6, sticky=W)
    lbl_contact = Label(addform, text="Contact", font=('arial', 14), bd=5)
    lbl_contact.grid(row=7, sticky=W)
    lbl_contact = Label(addform, text="Experiences", font=('arial', 14), bd=5)
    lbl_contact.grid(row=8, sticky=W)

    # ===================ENTRY===============================
    firstname = Entry(addform, width=20, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.grid(row=2, column=1)
    lastname = Entry(addform, width=20, textvariable=USERNAME, font=('arial', 14))
    lastname.grid(row=3, column=1)
    RadioGroup.grid(row=4, column=1)
    age = Entry(addform, width=20, textvariable=AGE, font=('arial', 14))
    age.grid(row=5, column=1)
    address = Entry(addform, width=20, textvariable=EADDRESS, font=('arial', 14))
    address.grid(row=6, column=1)
    contact = Entry(addform, width=20, textvariable=CONTACT, font=('arial', 14))
    contact.grid(row=7, column=1)
    contact = Entry(addform, width=20, textvariable=EXPERIENCE, font=('arial', 14))
    contact.grid(row=8, column=1)
    bsubmit = Button(addform, text="Submit Details", command=createdbadd, font=('arial', 14), width=20)
    bsubmit.grid(row=9, column=1)
    addform.mainloop()


# admin page which contains all modules of admin
def admin():
    root2 = Tk()
    root2.geometry('1300x600+70+70')
    root2.title("ADMIN PAGE")
    root2.configure(bg="yellow")
    tkm.showinfo("Login admin", "Login successful!!")

    lt = Label(root2, text="ADMIN PAGE", font=('arial', 36), bg='yellow')
    lt.place(x=500, y=100)
    b0 = Button(root2, text="+Add Member", command=addM, width=20, font=('arial', 14), fg='white', bg='black')
    b1 = Button(root2, text="Update Candidate's details", width=20, bg='black', fg='white', font=('arial', 14),
                command=updateC)
    b2 = Button(root2, text="View Employee Details", width=20, bg='black', fg='white', font=('arial', 14),
                command=viewC)
    b3 = Button(root2, text="Add Vacancy", bg='black', width=25, fg='white', font=('arial', 14), command=addV)
    b4 = Button(root2, text="View feedback and help", width=20, bg='black', fg='white', font=('arial', 14),
                command=viewfeed)

    Lc = Label(root2, text="Click here to", font=('arial', 8), bg="yellow").place(x=10, y=2)
    be = Button(root2, text="EXIT", command=lambda: aexit(root2), font=('arial', 14), bd=0, bg="yellow")
    be.place(x=10, y=18)
    b0.place(x=200, y=250)
    b1.place(x=500, y=250)
    b2.place(x=800, y=250)
    b3.place(x=330, y=400)
    b4.place(x=670, y=400)
    root2.mainloop()


# employee page which contains all modules of employee
def employee():
    root3 = Tk()
    root3.geometry('1350x700+70+70')
    root3.title("EMPLOYEE PAGE")
    root3.configure(bg="yellow")
    tkm.showinfo("Login employee", "Login successful!!")

    lt = Label(root3, text="EMPLOYEE PAGE", font=('arial', 36), bg='yellow')
    lt.place(x=500, y=100)
    b1 = Button(root3, text="Apply for a  job", command=applyforjob, width=20, font=('arial', 14), fg='white',
                bg='black')
    b2 = Button(root3, text="View vacancy", command=viewV, width=20, font=('arial', 14), fg='white', bg='black')
    b3 = Button(root3, text="Give Feedback", command=logfeedback, width=20, font=('arial', 14), fg='white', bg='black')
    b4 = Button(root3, text="Ask for help", command=askH, width=20, font=('arial', 14), fg='white', bg='black')
    b1.place(x=400, y=250)
    b2.place(x=400, y=400)
    b3.place(x=700, y=250)
    b4.place(x=700, y=400)


# ================Employee========================

# creating and connecting database for users
def create():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(
        "CREATE  TABLE IF NOT EXISTS users23(fname TEXT ,uname TEXT,password TEXT,Emid TEXT PRIMARY KEY, Phn int)")
    conn.commit()
    conn.close()


create()


# creating and connecting database for apllu ofr job
def create2():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(
        "CREATE  TABLE IF NOT EXISTS APLFORJOB(name TEXT ,age TEXT,phn TEXT,linkedin TEXT PRIMARY KEY, yearofexperience int,college TEXT)")
    conn.commit()
    conn.close()


create2()


# it is called when emloyee press for register
def Submitrr():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    x = (
                Fname.get() == "" or Uname.get() == "" or pswd.get() == "" or eid.get() == "" or phn.get() == "" or cpswd.get() == "")
    y = (pswd.get() != cpswd.get())
    if (x):
        tkm.showerror("Empty Field", "All the fields are required ")
        return
    if (y):
        tkm.showerror("Password", "password doesnt match")
        return
    else:
        try:
            c.execute("INSERT INTO users23(fname,uname,password,Emid,Phn) VALUES ('%s','%s','%s','%s','%s')" % (
            Fname.get(), Uname.get(), pswd.get(), eid.get(), phn.get()))
            conn.commit()
            label = Label(root, text=" Thankyou for registering ", font=('arabic', 30, 'bold'))
            label.place(x=290, y=450)
        except:
            messagebox.showerror(" Existing user ", "   USER already exisits ")


# it is called when when employee applys for job
def Submit2():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    x = (
                name.get() == "" or age.get() == "" or phn.get() == "" or lkd.get() == "" or Yof.get() == "" or college.get() == "")
    if (x):
        messagebox.showerror("Empty Field", "ALl the fields are required ", parent=root)
        return
    else:
        try:
            c.execute("INSERT INTO APLFORJOB VALUES ('%s','%s','%s','%s','%s','%s')" % (
            name.get(), age.get(), phn.get(), lkd.get(), Yof.get(), college.get()))
            conn.commit()
            label = Label(root, text=" Thankyou for registering ", font=('arabic', 30, 'bold'))
            label.place(x=290, y=450)
        except:
            messagebox.showerror(" Existing user ", "   USER already exisits ", parent=root)


# if employee is new user he register himself
def registration():
    rootr = Tk()
    rootr.geometry('800x600+50+50')
    label = Label(rootr, font=('arial', 10, 'bold'), bg='Light grey')
    label.pack(side='top', fill=X)
    label = Label(rootr, text=" Enter Your details ", font=('arial', 30, 'bold'), bg='Light grey')
    label.pack(side='top', fill=X)

    label = Label(rootr, font=('arial', 10, 'bold'), bg='Light grey')
    label.pack(side='top', fill=X)

    label = Label(rootr, font=('arial', 10, 'bold'), bg='Light grey', width=13)
    label.pack(side='left', fill=Y)

    label = Label(rootr, font=('arial', 10, 'bold'), bg='Light grey', width=13)
    label.pack(side='right', fill=Y)

    label = Label(rootr, font=('arial', 90, 'bold'), bg='Light grey', width=10)
    label.pack(side='bottom', fill=X)

    label = Label(rootr, text="Full Name:", font=('arial', 15, 'bold'))
    label.place(x=230, y=169)
    e1 = Entry(rootr, width=40, textvariable=Fname)
    e1.place(x=420, y=165, height=27)

    label = Label(rootr, text="Username:", font=('arial', 15, 'bold'))
    label.place(x=230, y=199)
    e1 = Entry(rootr, width=40, textvariable=Uname)
    e1.place(x=420, y=195, height=27)

    label = Label(rootr, text="Email Id:", font=('arial', 15, 'bold'))
    label.place(x=230, y=229)
    e1 = Entry(rootr, width=40, textvariable=eid)
    e1.place(x=420, y=225, height=27)

    label = Label(rootr, text="Phone number:", font=('arial', 15, 'bold'))
    label.place(x=230, y=259)
    e1 = Entry(rootr, width=40, textvariable=phn)
    e1.place(x=420, y=255, height=27)

    label = Label(rootr, text="Password:", font=('arial', 15, 'bold'))
    label.place(x=230, y=289)
    e1 = Entry(rootr, width=40, textvariable=pswd)
    e1.place(x=420, y=285, height=27)

    label = Label(rootr, text="Confirm password:", font=('arial', 15, 'bold'))
    label.place(x=230, y=319)
    e1 = Entry(rootr, width=40, textvariable=cpswd)
    e1.place(x=420, y=315, height=27)
    button = Button(rootr, text="Submit", font=('arial', 10, 'bold'), bg='light grey', activebackground='grey',
                    command=Submitrr)
    button.place(x=475, y=375, width=190)
    rootr.mainloop()


# if employee is existing employee he will login with his credentials
def login():
    rootl = Tk()
    rootl.geometry('800x600+50+50')
    label = Label(rootl, font=('arial', 10, 'bold'), bg='Light grey')
    label.pack(side='top', fill=X)

    label = Label(rootl, text=" Log in ", font=('arial', 30, 'bold'), bg='Light grey')
    label.pack(side='top', fill=X)

    label = Label(rootl, font=('arial', 10, 'bold'), bg='Light grey')
    label.pack(side='top', fill=X)

    label = Label(rootl, font=('arial', 10, 'bold'), bg='Light grey', width=13)
    label.pack(side='left', fill=Y)

    label = Label(rootl, font=('arial', 10, 'bold'), bg='Light grey', width=13)
    label.pack(side='right', fill=Y)

    label = Label(rootl, font=('arial', 90, 'bold'), bg='Light grey', width=10)
    label.pack(side='bottom', fill=X)

    label = Label(rootl, text="Username:", font=("itlaic", 12, "bold"))
    label.place(x=150, y=240)
    e1 = Entry(rootl, width=50)
    e1.place(x=250, y=240, height=25)

    label = Label(rootl, text="Password:", font=("itlaic", 12, "bold"))
    label.place(x=150, y=265)
    e1 = Entry(rootl, width=50)
    e1.place(x=250, y=265, height=25)

    button = Button(rootl, text="Log in", font=('arabic', 10, 'bold'), activebackground='grey', width=20,
                    command=employee)
    button.place(x=300, y=320)
    rootl.mainloop()


# employee applies for a job
def applyforjob():
    roota = Tk()
    roota.geometry('800x600+50+50')
    label = Label(roota, font=('arial', 10, 'bold'), bg='Light grey')
    label.pack(side='top', fill=X)

    label = Label(roota, text=" Enter Your details ", font=('arial', 30, 'bold'), bg='Light grey')
    label.pack(side='top', fill=X)

    label = Label(roota, font=('arial', 10, 'bold'), bg='Light grey')
    label.pack(side='top', fill=X)

    label = Label(roota, font=('arial', 10, 'bold'), bg='Light grey', width=13)
    label.pack(side='left', fill=Y)

    label = Label(roota, font=('arial', 10, 'bold'), bg='Light grey', width=13)
    label.pack(side='right', fill=Y)

    label = Label(roota, font=('arial', 90, 'bold'), bg='Light grey', width=10)
    label.pack(side='bottom', fill=X)

    label = Label(roota, text="Name:", font=('arial', 15, 'bold'))
    label.place(x=230, y=169)
    e1 = Entry(roota, width=40, textvariable=name)
    e1.place(x=420, y=165, height=27)

    label = Label(roota, text="Age:", font=('arial', 15, 'bold'))
    label.place(x=230, y=199)
    e1 = Entry(roota, width=40, textvariable=age)
    e1.place(x=420, y=195, height=27)
    label = Label(roota, text="Phone number:", font=('arial', 15, 'bold'))
    label.place(x=230, y=259)
    e1 = Entry(roota, width=40, textvariable=phn)
    e1.place(x=420, y=255, height=27)

    label = Label(roota, text="LinkedIN", font=('arial', 15, 'bold'))
    label.place(x=230, y=289)
    e1 = Entry(roota, width=40, textvariable=lkd)
    e1.place(x=420, y=285, height=27)

    label = Label(roota, text="year of experiece ", font=('arial', 15, 'bold'))
    label.place(x=230, y=319)
    e1 = Entry(roota, width=40, textvariable=Yof)
    e1.place(x=420, y=315, height=27)

    label = Label(roota, text="College ", font=('arial', 15, 'bold'))
    label.place(x=230, y=349)
    e1 = Entry(roota, width=40, textvariable=college)
    e1.place(x=420, y=345, height=27)

    button = Button(roota, text="Submit", font=('arial', 10, 'bold'), bg='light grey', activebackground='grey',
                    command=Submit2)
    button.place(x=475, y=375, width=190)
    roota.mainloop()


# ======================ROOT===================================

# creating main root
root1 = Tk()
root1.geometry('1300x600+100+100')
root1.title("USER")
root1.resizable(False, False)

img2 = ImageTk.PhotoImage(Image.open("Untitled2.jpg"))
lb2 = Label(root1, image=img2)
lb2.image = img2
lb2.place(x=70, y=70)

f1 = Frame(root1, bg="white")
f1.place(x=750, y=150, width=350, height=300)
root1.configure(bg="black")
img1 = ImageTk.PhotoImage(Image.open("YiRe2G.jpg"))
lb1 = Label(f1, image=img1)
lb1.image = img1
lb1.place(x=0, y=0, relwidth=1, relheight=1)

# ============================VARIABLES===================================
FIRSTNAME = StringVar()
USERNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
EADDRESS = StringVar()
CONTACT = StringVar()
username = StringVar()
usernameL = StringVar()
passwordL = StringVar()
usernameE = StringVar()
password = StringVar()
passwordE = StringVar()
fullname = StringVar()
username = StringVar()
eid = StringVar()
phonenum = StringVar()
passw1 = StringVar()
passw2 = StringVar()
UPDATENAME = StringVar()
NEWNAME = StringVar()
NEWUSERNAME = StringVar()
NEWID = StringVar()
NEWPHONE = StringVar()
EXPERIENCE = StringVar()
FIELD = StringVar()
EXPER = StringVar()
SKILL = StringVar()
COMPANY = StringVar()
INDUSTRY = StringVar()
PLACE = StringVar()
ROLE = StringVar()
FEEDMAIL = StringVar()
FEEDQUERY = StringVar()
Fname = StringVar()
Uname = StringVar()
phn = StringVar()
pswd = StringVar()
cpswd = StringVar()
name = StringVar()
age = StringVar()
phn = StringVar()
lkd = StringVar()
Yof = StringVar()
college = StringVar()

lb1 = Label(f1, text="TYPE OF USER", bg="white", font=('arial', 16))
lb1.place(x=100, y=50)

b1 = Button(f1, text="Admin", font=('arial', 10, 'bold'), width=20, height=2, command=login_admin).place(x=100, y=125)
b2 = Button(f1, text="Employee", font=('arial', 10, 'bold'), width=20, height=2, command=login_employee).place(x=100,
                                                                                                               y=225)

root1.mainloop()
