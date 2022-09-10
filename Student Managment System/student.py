from os import execv
from tkinter import*
from tkinter import ttk
from tkinter import font
from types import resolve_bases
from PIL import Image,ImageTk #pip install pillow
import mysql.connector 
from tkinter import messagebox
class Student :
    def __init__(self, root):

        self.root = root
        self.root.geometry("1400x690+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")


    #Variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semster=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mobile_no=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


    #1st image
        img = Image.open(r"images\pink background.jpg")
        img = img.resize((510,160),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=510,height=160)

    #2nd image
        img_2 = Image.open(r"images\pink background.jpg")
        img_2 = img_2.resize((510,160),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=510,y=0,width=510,height=160)

    #3rd image
        img_3 = Image.open(r"images\pink background.jpg")
        img_3 = img_3.resize((510,160),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=1000,y=0,width=510,height=160)

    #bg image 
        img_4 = Image.open(r"images\bgimage.jpg")
        img_4 = img_4.resize((1450,710),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_lable = Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lable.place(x=0,y=100,width=1450,height=710)

        lbl_title =Label(bg_lable, text="STUDENT MANAGMENT SYSTEM",font=("times new roman",37,"bold"),fg="blue",bg="white")
        lbl_title.place(x=0,y=0,width=1450,height=50)           #uppar ke 3 photo + bg image which is not visible lol


    #manage frame
        Manage_frame=Frame(bg_lable,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=0,y=50,width=1450,height=560)             #main frame - isi ke andar sab frame banaye hai

        #left frame
        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        DataLeftFrame.place(x=10,y=10,width=650,height=520)

        #img in keft frame

        img_5 = Image.open(r"images\light pink image.jpg")
        img_5 = img_5.resize((650,120),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_img = Label(DataLeftFrame,image=self.photoimg_5,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=640,height=120)

        # Current course Information LabelFrame 

        std_lbl_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current course LabelFrame Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_info_frame.place(x=0,y=120,width=640,height=115)

        #Lables

        #dept label
        lbl_dept=Label(std_lbl_info_frame,text="Department",font=("arial",12,"bold"),bg="white")
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)

        combo_dept=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dept["value"]=("Select Depeatmant","Computer","IT","Civil")
        combo_dept.current(0)
        combo_dept.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #courses
        course_std=Label(std_lbl_info_frame,text="Course",font=("arial",12,"bold"),bg="white")
        course_std.grid(row=0,column=2,padx=2,sticky=W,pady=10)

        combo_course=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_course,font=("arial",12,"bold"),width=17,state="readonly")
        combo_course["value"]=("Select Course","FE","SE","TE","BE")
        combo_course.current(0)
        combo_course.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_lable=Label(std_lbl_info_frame,text="Year",font=("arial",12,"bold"),bg="white")
        year_lable.grid(row=1,column=0,padx=2,sticky=W,pady=10)

        combo_year=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year,font=("arial",12,"bold"),width=17,state="readonly")
        combo_year["value"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        combo_year.current(0)
        combo_year.grid(row=1,column=1,padx=2,sticky=W)

        #semester
        lbl_semester=Label(std_lbl_info_frame,text="Semester",font=("arial",12,"bold"),bg="white")
        lbl_semester.grid(row=1,column=2,padx=2,sticky=W,pady=10)

        combo_semester=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_semster,font=("arial",12,"bold"),width=17,state="readonly")
        combo_semester["value"]=("Select Semester","1","2","3","4","5","6","7","8")
        combo_semester.current(0)
        combo_semester.grid(row=1,column=3,padx=2,sticky=W,pady=10) #---end of combo box vala frame

        #student class information lable
        std_class_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Student class course information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_class_info_frame.place(x=0,y=240,width=640,height=220)

        #labels and label entry
        lbl_Id=Label(std_class_info_frame,text="Student Id:",font=("arial",12,"bold"),bg="white")
        lbl_Id.grid(row=0,column=0,padx=2,sticky=W,pady=7)

        id_entry = ttk.Entry(std_class_info_frame,textvariable=self.var_std_id,font=("arial",12,"bold"),width=15)
        id_entry.grid(row=0,column=1,padx=2,sticky=W,pady=7)
        #Name
        lbl_name=Label(std_class_info_frame,text="Student name:",font=("arial",12,"bold"),bg="white")
        lbl_name.grid(row=0,column=2,padx=2,sticky=W,pady=7)

        name_entry = ttk.Entry(std_class_info_frame,textvariable=self.var_std_name,font=("arial",12,"bold"),width=15)
        name_entry.grid(row=0,column=3,padx=2,sticky=W,pady=7)
        
        #division
        lbl_division=Label(std_class_info_frame,text="Student division:",font=("arial",12,"bold"),bg="white")
        lbl_division.grid(row=1,column=0,padx=2,sticky=W,pady=7)

        combo_division=ttk.Combobox(std_class_info_frame,textvariable=self.var_div,font=("arial",12,"bold"),width=17,state="readonly")
        combo_division["value"]=("Select division","A","B","C")
        combo_division.current(0)
        combo_division.grid(row=1,column=1,padx=2,sticky=W,pady=7)
        
        #roll no
        lbl_rollno=Label(std_class_info_frame,text="Student rollno:",font=("arial",12,"bold"),bg="white")
        lbl_rollno.grid(row=1,column=2,padx=2,sticky=W,pady=7)

        rollno_entry = ttk.Entry(std_class_info_frame,textvariable=self.var_roll,font=("arial",12,"bold"),width=15)
        rollno_entry.grid(row=1,column=3,padx=2,sticky=W,pady=7)

        #gender
        ldl_gender=Label(std_class_info_frame,text="Student gender:",font=("arial",12,"bold"),bg="white")
        ldl_gender.grid(row=2,column=0,padx=2,sticky=W,pady=7)

        combo_gender=ttk.Combobox(std_class_info_frame,textvariable=self.var_gender,font=("arial",12,"bold"),width=17,state="readonly")
        combo_gender["value"]=("Select Gender","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1,padx=2,sticky=W,pady=7)

        #dob
        lbl_dob=Label(std_class_info_frame,text="Student DOB:",font=("arial",12,"bold"),bg="white")
        lbl_dob.grid(row=2,column=2,padx=2,sticky=W,pady=7)

        dob_entry = ttk.Entry(std_class_info_frame,textvariable=self.var_dob,font=("arial",12,"bold"),width=15)
        dob_entry.grid(row=2,column=3,padx=2,sticky=W,pady=7)

        #email
        lbl_email=Label(std_class_info_frame,text="Student email:",font=("arial",12,"bold"),bg="white")
        lbl_email.grid(row=3,column=0,padx=2,sticky=W,pady=7)

        email_entry = ttk.Entry(std_class_info_frame,textvariable=self.var_email,font=("arial",12,"bold"),width=15)
        email_entry.grid(row=3,column=1,padx=2,sticky=W,pady=7)

        #modile_no
        lbl_modile_no=Label(std_class_info_frame,text="Student modile_no:",font=("arial",12,"bold"),bg="white")
        lbl_modile_no.grid(row=3,column=2,padx=2,sticky=W,pady=7)

        modile_no_entry = ttk.Entry(std_class_info_frame,textvariable=self.var_mobile_no,font=("arial",12,"bold"),width=15)
        modile_no_entry.grid(row=3,column=3,padx=2,sticky=W,pady=7)

        #address
        lbl_address=Label(std_class_info_frame,text="Student address:",font=("arial",12,"bold"),bg="white")
        lbl_address.grid(row=4,column=0,padx=2,sticky=W,pady=7)

        address_entry = ttk.Entry(std_class_info_frame,textvariable=self.var_address,font=("arial",12,"bold"),width=15)
        address_entry.grid(row=4,column=1,padx=2,sticky=W,pady=7)

        #teacher
        lbl_teacher=Label(std_class_info_frame,text="Student teacher:",font=("arial",12,"bold"),bg="white")
        lbl_teacher.grid(row=4,column=2,padx=2,sticky=W,pady=7)

        teacher_entry = ttk.Entry(std_class_info_frame,textvariable=self.var_teacher,font=("arial",12,"bold"),width=15)
        teacher_entry.grid(row=4,column=3,padx=2,sticky=W,pady=7)
        
        #Buttons with frame

        #frame
        button_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=460.5,width=640,height=28) 

        #save button
        btn_Add = Button(button_frame,text="Save",command=self.add_data,font=("arial",10,"bold"),width=18,bg="blue",fg="white") #command=self.add_data,
        btn_Add.grid(row = 0, column=0,padx=2)

        #update button
        btn_update = Button(button_frame,text="Update",command=self.update_data,font=("arial",10,"bold"),width=18,bg="blue",fg="white")
        btn_update.grid(row = 0, column=1,padx=2)

        #delete button
        btn_delete = Button(button_frame,text="Delete",command=self.delete_data,font=("arial",10,"bold"),width=18,bg="blue",fg="white")
        btn_delete.grid(row = 0, column=2,padx=2)

        #reset button
        btn_reset = Button(button_frame,text="Reset",command=self.reset_data,font=("arial",10,"bold"),width=18,bg="blue",fg="white")
        btn_reset.grid(row = 0, column=3,padx=2)

        #right frame
        DataRightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        DataRightFrame.place(x=670,y=10,width=670,height=520)

        img_6 = Image.open(r"images\light pink image.jpg")
        img_6 = img_6.resize((780,200),Image.ANTIALIAS)
        self.photoimg_6=ImageTk.PhotoImage(img_6)

        my_img = Label(DataRightFrame,image=self.photoimg_6,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=660.5,height=200)

        #search frame
        Search_Frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Search student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        Search_Frame.place(x=0,y=200,width=660.5,height=50.5)

        Search_by=Label(Search_Frame,text="Search by",font=("arial",11,"bold"),bg="Blue",fg="white")
        Search_by.grid(row=0,column=0,padx=5,sticky=W)

        self.var_combo_search=StringVar()
        combo_search=ttk.Combobox(Search_Frame,textvariable=self.var_combo_search,font=("arial",12,"bold"),width=17,state="readonly")
        combo_search["value"]=("Select Option","Roll No","Mobile No","Student Id")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2,sticky=W)
        
        self.var_search=StringVar()
        txt_search_entrt= ttk.Entry(Search_Frame,textvariable=self.var_search,font=("arial",12,"bold"),width=15)
        txt_search_entrt.grid(row=0,column=2,padx=2,sticky=W)

        btn_search = Button(Search_Frame,command=self.search_data,text="Search",font=("arial",10,"bold"),width=13,bg="blue",fg="white")
        btn_search.grid(row = 0, column=3,padx=3)

        btn_showall = Button(Search_Frame,command=self.fetch_data,text="Show All",font=("arial",10,"bold"),width=13,bg="blue",fg="white")
        btn_showall.grid(row = 0, column=4,padx=2)

        #================Student Table and Scroll Bar====================

        #frame
        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=250.5,width=660.5,height=240)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","mobile no"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semster")
        self.student_table.heading("id",text="Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("mobile no",text="Mobile No")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("mobile no",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if (self.var_dep.get()=="" or self.var_std_id.get()==""or self.var_email.get()==""):
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Tanvi@03",database="my_data")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                            (
                                                            self.var_dep.get(),
                                                            self.var_course.get(),
                                                            self.var_year.get(),
                                                            self.var_semster.get(),
                                                            self.var_std_id.get(),
                                                            self.var_std_name.get(),
                                                            self.var_div.get(),
                                                            self.var_roll.get(),
                                                            self.var_gender.get(),
                                                            self.var_dob.get(),
                                                            self.var_email.get(),
                                                            self.var_mobile_no.get(),
                                                            self.var_address.get(),
                                                            self.var_teacher.get()

                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added",parent=self.root)
            except Exception as es : 
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
               
    #fetch function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Tanvi@03",database="my_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select *from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semster.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_mobile_no.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])

    def update_data(self):
        if (self.var_dep.get()=="" or self.var_std_id.get()==""or self.var_email.get()==""):
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure to update this student data",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Tanvi@03",database="my_data")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,course=%s,year=%s,course=%s,Semester=%s,Name=%s,Division=%s,Roll no=%s,Gender=%s,Email=%s,Mobile=%s,address=%s,Teacher=%s where student_id=%s",
                                                                    (
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semster.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_mobile_no.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_std_id.get()

                                                                                                            ))
                else:
                    if not update:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","Successfully updated the data",parent=self.root) 
            except Exception as es : 
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
   
    #delete 
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are sure to delete this students",parent=self.root)
                if Delete>0 :
                    conn=mysql.connector.connect(host="localhost",username="root",password="Tanvi@03",database="my_data")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    value=(self.var_std_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Data has been deleted",parent=self.root)
            except Exception as es : 
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #reset
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_course.set("select course")
        self.var_year.set("select year")
        self.var_semster.set("select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_mobile_no.set("")
        self.var_address.set("")
        self.var_teacher.set("")

    #search  
    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Tanvi@03",database="my_data")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from students where " +str(self.var_combo_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=1)
                        conn.commit()
                    conn.close()
            except Exception as es : 
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
   

        

               



                                                                                                      
                                                                                          

        

                                                            


        



if __name__ == "__main__":
    root =Tk()
    obj=Student(root)
    root.mainloop()

    #update and search button showing error and last part of video is remaining...or else the project is done!!! lol it took me 3 days..but still
    #isn't complete yet...I'll do it whenever I'll feel to 