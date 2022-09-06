from tkinter import *
from tkinter import ttk,messagebox
import pymysql
import qrcode
import os
from PIL import ImageTk
from resizeimage import resizeimage

class mang_student:
    def __init__(self,root):
        self.root=root
        self.root.title("Manage Student")
        self.root.geometry("1055x525+215+120")
        self.root.resizable(0,0)
        self.root.focus_force()
        self.root.grab_set()
        self.root.config(bg="light blue")
        self.root.iconbitmap("images/icon1.ico")

        #==================frame 1====================================================================================================
        frame1=LabelFrame(self.root,text="Students Details",font=("times new roman",13),fg="peru",bg="snow",bd=3,relief=RAISED)
        frame1.place(x=1,y=1,width=750,height=300)
        #==========Student Details====================================
        self.regd_no_var1=StringVar()
        self.name_var1=StringVar()
        self.fname_var1=StringVar()
        self.email_var1=StringVar()
        self.dob_var1=StringVar()
        self.gender_var1=StringVar()
        self.course_var1=StringVar()
        self.con1_var1=StringVar()
        self.blood_var1=StringVar()
        
        regd_no_lbl=Label(frame1,text="Registration no.",font=("times new roman",15),bg="snow",fg="#262626").place(x=10,y=25)
        regd_no_txt=Entry(frame1,textvariable=self.regd_no_var1,font=("times new roman",15),state="readonly",bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=160,y=25,width=180,height=28)

        name_lbl=Label(frame1,text="Student's Name",font=("times new roman",15),bg="snow",fg="#262626").place(x=380,y=25)
        name_txt=Entry(frame1,textvariable=self.name_var1,font=("times new roman",15),state="readonly",bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=540,y=25,width=180,height=28)

        father_name_lbl=Label(frame1,text="Father's Name",font=("times new roman",15),bg="snow",fg="#262626").place(x=10,y=70)
        father_name_txt=Entry(frame1,textvariable=self.fname_var1,font=("times new roman",15),state="readonly",bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=160,y=70,width=180,height=28)

        email_lbl=Label(frame1,text="E_mail Id",font=("times new roman",15),bg="snow",fg="#262626").place(x=380,y=70)
        email_txt=Entry(frame1,textvariable=self.email_var1,font=("times new roman",15),state="readonly",bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=540,y=70,width=180,height=28)

        dob=Label(frame1,text="Date of Birth",font=("times new roman",15),bg="snow",fg="#262626").place(x=10,y=110)
        dob_txt=Entry(frame1,textvariable=self.dob_var1,font=("times new roman",15),state="readonly",bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=160,y=110,width=180,height=28)

        gender_lbl=Label(frame1,text="Gender",font=("times new roman",15),bg="snow",fg="#262626").place(x=380,y=110)
        gender_txt=Entry(frame1,textvariable=self.gender_var1,font=("times new roman",15),state="readonly",bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=540,y=110,width=180,height=28)

        course=Label(frame1,text="Course",font=("times new roman",15),bg="snow",fg="#262626").place(x=10,y=150)
        course_txt=Entry(frame1,textvariable=self.course_var1,font=("times new roman",15),state="readonly",bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=160,y=150,width=180,height=28)

        con_lbl=Label(frame1,text="Contact",font=("times new roman",15),bg="snow",fg="#262626").place(x=380,y=150)
        con_txt=Entry(frame1,textvariable=self.con1_var1,font=("times new roman",15),state="readonly",bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=540,y=150,width=180,height=28)

        blood=Label(frame1,text="Blood Group",font=("times new roman",15),bg="snow",fg="#262626").place(x=10,y=190)
        blood_txt=Entry(frame1,textvariable=self.blood_var1,font=("times new roman",15),state="readonly",bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=160,y=190,width=180,height=28)

        #=======Buttons=====frame1==================
        gen_btn=Button(frame1,command=self.generate_qr,text="Generate QR",font=("times new roman",18,"bold"),bd=2,relief=RAISED,bg="light green",fg="black",activebackground="green",activeforeground="white",cursor="hand2").place(x=10,y=230,width=200,height=30)
        clear_btn=Button(frame1,command=self.clear_student1,text="Clear",font=("times new roman",18,"bold"),bd=2,relief=RAISED,bg="orange",fg="black",activebackground="black",activeforeground="orange",cursor="hand2").place(x=220,y=230,width=120,height=30)
        
        self.msg=""
        self.lbl_msg=Label(frame1,text=self.msg,font=("times new roman",20),bg="snow",fg="green")
        self.lbl_msg.place(x=360,y=210,width=350)
        #=================================================================================================================================================================================

        #==================frame 2====================================================================================================
        frame2=LabelFrame(self.root,text="ID card",font=("times new roman",13),bg="snow",fg="peru",bd=3,relief=RAISED)
        frame2.place(x=751,y=1,width=300,height=300)

        self.qr_code=Label(frame2,text="No QR \nAvailable",font=("times new roman",16),bd=0,relief=RIDGE,bg="#0000CD",fg="white")
        self.qr_code.place(x=30,y=20,width=230,height=230)
        #=================================================================================================================================================================================

        #==================frame 3====================================================================================================
        frame3=LabelFrame(self.root,text="Search Student",font=("times new roman",13),fg="peru",bg="snow",bd=3,relief=RAISED)
        frame3.place(x=1,y=302,width=1050,height=70)
        self.search_by_var=StringVar()
        self.search_txt_var=StringVar()

        search_lbl=Label(frame3,text="Search By :",font=("times new roman",20,"bold"),bg="snow",fg="red").place(x=20,y=0)

        search_by_cmb=ttk.Combobox(frame3,textvariable=self.search_by_var,font=("times new roman",15),state="readonly",justify="center")
        search_by_cmb['values']=("Search By","`Regd. No.`","`Name`","`E_mail id`","`Section`","`Contact1`","`Contact2`")
        search_by_cmb.current(0)
        search_by_cmb.place(x=200,y=5,width=180,height=28)

        search_txt=Entry(frame3,textvariable=self.search_txt_var,font=("times new roman",15),bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=420,y=5,width=200,height=28)

        search_btn=Button(frame3,command=self.search_data,text="Search",font=("times new roman",18,"bold"),bd=2,relief=RAISED,bg="white",fg="black",activebackground="black",activeforeground="white",cursor="hand2").place(x=650,y=4,width=150,height=30)
        showall_btn=Button(frame3,command=self.fetch_data,text="Show All",font=("times new roman",18,"bold"),bd=2,relief=RAISED,bg="white",fg="black",activebackground="black",activeforeground="white",cursor="hand2").place(x=830,y=4,width=170,height=30)
        #=================================================================================================================================================================================
        
        #==================frame 4====================================================================================================
        student_frame=Frame(self.root,bg="green",bd=3,relief=RAISED)
        student_frame.place(x=1,y=372,width=1050,height=150)
        
        scroll_x = Scrollbar(student_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(student_frame,orient=VERTICAL)
        self.Student_table = ttk.Treeview(student_frame,column=("admid","date","reg_no","name","fname","mname","foccu","email","dob","gender","course","section","con1","con2","blood","religion","address","face"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("admid",text="Addmission ID")
        self.Student_table.heading("date",text="Addmission Date")
        self.Student_table.heading("reg_no",text="Regd. No.")
        self.Student_table.heading("name",text="Student Name")
        self.Student_table.heading("fname",text="Father's Name")
        self.Student_table.heading("mname",text="Mother's Name")
        self.Student_table.heading("foccu",text="Father's Occupation")
        self.Student_table.heading("email",text="E_mail ID")
        self.Student_table.heading("dob",text="Date of Birth")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("course",text="Course")
        self.Student_table.heading("section",text="Section")
        self.Student_table.heading("con1",text="Contact No")
        self.Student_table.heading("con2",text="Alternate No.")
        self.Student_table.heading("blood",text="Blood Group")
        self.Student_table.heading("religion",text="Religion")
        self.Student_table.heading("address",text="Address")
        self.Student_table.heading("face",text="Face Photo")
        self.Student_table['show']='headings'
        self.Student_table.column("admid",width=180)
        self.Student_table.column("date",width=180)
        self.Student_table.column("reg_no",width=180)
        self.Student_table.column("name",width=200)
        self.Student_table.column("fname",width=200)
        self.Student_table.column("mname",width=200)
        self.Student_table.column("foccu",width=190)
        self.Student_table.column("email",width=200)
        self.Student_table.column("dob",width=180)
        self.Student_table.column("gender",width=170)
        self.Student_table.column("course",width=180)
        self.Student_table.column("section",width=170)
        self.Student_table.column("con1",width=200)
        self.Student_table.column("con2",width=200)
        self.Student_table.column("blood",width=160)
        self.Student_table.column("religion",width=170)
        self.Student_table.column("address",width=230)
        self.Student_table.column("face",width=160)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.pack()
        self.fetch_data()
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

#===========creating folder==========================
        if os.path.exists('Students QR_Code')==False:
            os.mkdir('Students QR_Code')
#=================================================================================================================================================================================
    def fetch_data(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
            cur=con.cursor()
            cur.execute("select * from add_student")
            rows=cur.fetchall()
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def search_data(self):
        if self.search_by_var.get()=="Search By":
            messagebox.showerror("Error","Please select the search type ?",parent=self.root)
        elif self.search_txt_var.get()=="":
            messagebox.showerror("Error","Search field must be filled as per the search type !!",parent=self.root)
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
            cur=con.cursor()
            cur.execute("select * from add_student where"+str(self.search_by_var.get())+" LIKE '%"+str(self.search_txt_var.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert("",END,values=row)
            con.commit()
            con.close()


    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.regd_no_var1.set(row[2])
        self.name_var1.set(row[3])
        self.fname_var1.set(row[4])
        self.email_var1.set(row[7])
        self.dob_var1.set(row[8])
        self.gender_var1.set(row[9])
        self.course_var1.set(row[10])
        self.con1_var1.set(row[12])
        self.blood_var1.set(row[14])


    def generate_qr(self):
        if self.regd_no_var1.get()=="" or self.name_var1.get()=="" or self.fname_var1.get()=="Select" or self.con1_var1.get()=="" or self.dob_var1.get()=="" or self.gender_var1.get()=="Select":
            self.msg="All Fields are Required ⁉"
            self.lbl_msg.config(text=self.msg,fg="red")
        else:
            qr_data=(f"Registration No: {self.regd_no_var1.get()}\nStudent Name: {self.name_var1.get()}\nFather's Name: {self.fname_var1.get()}\nE_mail Id: {self.email_var1.get()}\nD.O.B Id: {self.dob_var1.get()}\nGender: {self.gender_var1.get()}\nCourse: {self.course_var1.get()}\nContact: {self.con1_var1.get()}\nBlood Group: {self.blood_var1.get()}" )
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[230,230])
            qr_code.save("Students QR_Code/Regd No._"+str(self.regd_no_var1.get())+".png")

            self.im=PhotoImage(file="Students QR_Code/Regd No._"+str(self.regd_no_var1.get())+".png")
            self.qr_code.config(image=self.im)

            self.msg="  QR Generated Suceessfully!!!"
            self.lbl_msg.config(text=self.msg,fg="green")
   
    
    def clear_student1(self):
        self.regd_no_var1.set("")
        self.name_var1.set("")
        self.fname_var1.set("")
        self.email_var1.set("")
        self.dob_var1.set("")
        self.gender_var1.set("")
        self.course_var1.set("")
        self.con1_var1.set("")
        self.blood_var1.set("")
        self.msg=""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image="")
        self.search_by_var.set("Search By")
        self.search_txt_var.set("")
        self.fetch_data()


if __name__=="__main__":
    root=Tk()
    object=mang_student(root)
    root.mainloop()