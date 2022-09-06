from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
import os
import csv
import pymysql

my_data=[]

class attendance:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance Management System")
        self.root.geometry("1280x650+0+0")
        self.root.grab_set()
        self.root.focus()
        self.root.iconbitmap("images/icon3.ico")
        self.root.resizable(0,0)

        title=Label(self.root,text="    Attendance Report",font=("times new roman",35,"bold"),bd=3,relief=RAISED,bg="cyan",fg="black",anchor=W).place(x=0,y=1,relwidth=1)
        
        self.id_var=StringVar()
        self.regd_var=StringVar()
        self.name_var=StringVar()
        self.branch_var=StringVar()
        self.time_var=StringVar()
        self.date_var=StringVar()
        self.status_var=StringVar()
        self.search_by_var=StringVar()
        self.search_txt_var=StringVar()

        frame1=Frame(self.root,bd=3,relief=RIDGE,bg="light green")
        frame1.place(x=3,y=63,width=480,height=585)

        label_upadate=Label(frame1,text="Update Attendance",font=("times new roman",25,"bold"),bg="white",fg="blue").place(x=0,y=10,relwidth=1)

        label_regd=Label(frame1,text="Attendance Id",font=("times new roman",20,"bold"),bg="light green",fg="black").place(x=0,y=60)
        label_regd=Label(frame1,text="Registration No.",font=("times new roman",20,"bold"),bg="light green",fg="black").place(x=0,y=100)
        label_name=Label(frame1,text="Name",font=("times new roman",20,"bold"),bg="light green",fg="black").place(x=0,y=140)
        label_branch=Label(frame1,text="Branch",font=("times new roman",20,"bold"),bg="light green",fg="black").place(x=0,y=180)
        label_time=Label(frame1,text="Time",font=("times new roman",20,"bold"),bg="light green",fg="black").place(x=0,y=220)
        label_date=Label(frame1,text="Date(dd/mm/yyyy)",font=("times new roman",20,"bold"),bg="light green",fg="black").place(x=0,y=260)
        label_attendance_status=Label(frame1,text="Attendance Status",font=("times new roman",20,"bold"),bg="light green",fg="black").place(x=0,y=300)

        id_txt=Entry(frame1,textvariable=self.id_var,font=("times new roman",18),state=DISABLED,bd=3,relief=SUNKEN,bg="light yellow").place(x=240,y=64,width=220,height=30)
        regd_txt=Entry(frame1,textvariable=self.regd_var,font=("times new roman",18),bd=3,relief=SUNKEN,bg="light yellow").place(x=240,y=102,width=220,height=30)
        name_txt=Entry(frame1,textvariable=self.name_var,font=("times new roman",18),bd=3,relief=SUNKEN,bg="light yellow").place(x=240,y=142,width=220,height=30)
        branch_txt=Entry(frame1,textvariable=self.branch_var,font=("times new roman",18),bd=3,relief=SUNKEN,bg="light yellow").place(x=240,y=182,width=220,height=30)
        time_txt=Entry(frame1,textvariable=self.time_var,font=("times new roman",18),bd=3,relief=SUNKEN,bg="light yellow").place(x=240,y=222,width=220,height=30)
        date_txt=Entry(frame1,textvariable=self.date_var,font=("times new roman",18),bd=3,relief=SUNKEN,bg="light yellow").place(x=240,y=262,width=220,height=30)
        attendance_cmb=ttk.Combobox(frame1,textvariable=self.status_var,font=("times new roman",16),state="readonly",justify="center")
        attendance_cmb['values']=("Select","Present","Absent")
        attendance_cmb.current(0)
        attendance_cmb.place(x=240,y=302,width=220,height=30)

        btn_add=Button(frame1,command=self.add_attendance,text="Add",font=("times new roman",20,"bold"),bd=2,relief=RAISED,cursor="hand2",bg="black",fg="white",activebackground="green",activeforeground="black").place(x=40,y=350,width=150,height=35)
        btn_update=Button(frame1,command=self.update_attendance,text="Update",font=("times new roman",20,"bold"),bd=2,relief=RAISED,cursor="hand2",bg="black",fg="white",activebackground="orange",activeforeground="black").place(x=250,y=350,width=150,height=35)
        btn_delete=Button(frame1,command=self.delete_attendance,text="Delete",font=("times new roman",20,"bold"),bd=2,relief=RAISED,cursor="hand2",bg="black",fg="white",activebackground="red",activeforeground="black").place(x=40,y=400,width=150,height=35)
        btn_clear=Button(frame1,command=self.clear_table,text="Clear",font=("times new roman",20,"bold"),bd=2,relief=RAISED,cursor="hand2",bg="black",fg="white",activebackground="purple",activeforeground="black").place(x=250,y=400,width=150,height=35)

        label_export=Label(frame1,text="Import & Export Excel file",font=("times new roman",20,"bold"),bg="white",fg="blue").place(x=0,y=450,relwidth=1)

        btn_import1 = Button(frame1,command=self.import_csv, text="Import\nExcel File", font=("times new roman", 18, "bold"), bd=2, relief=RAISED,
                            cursor="hand2", bg="black", fg="white", activebackground="orange",
                            activeforeground="black").place(x=40, y=500, width=160, height=60)
        btn_export2 = Button(frame1,command=self.export_csv, text="Export\nExcel File", font=("times new roman", 18, "bold"), bd=2, relief=RAISED,
                           cursor="hand2", bg="black", fg="white", activebackground="purple",
                           activeforeground="black").place(x=250, y=500, width=160, height=60)


        frame2 = Frame(self.root, bd=3, relief=RIDGE,bg="light green")
        frame2.place(x=488, y=63, width=790, height=585)

        search_lbl=Label(frame2,text="Search By:",font=("times new roman",22,"bold"),bg="light green",fg="black").place(x=5,y=10)

        search_cmb = ttk.Combobox(frame2,textvariable=self.search_by_var, font=("times new roman", 16), state="readonly", justify="center")
        search_cmb['values'] = ("Select Option", "`Regd. No.`", "`Name`","`Branch`","`Date`")
        search_cmb.current(0)
        search_cmb.place(x=155, y=14, width=170, height=30)

        search_txt=Entry(frame2,textvariable=self.search_txt_var,font=("times new roman",18),bd=3,relief=SUNKEN,bg="light yellow").place(x=340,y=14,width=180,height=30)

        btn_search = Button(frame2,command=self.search_data, text="Search", font=("times new roman", 18, "bold"), bd=2, relief=RAISED,
                            cursor="hand2", bg="black", fg="white", activebackground="white",
                            activeforeground="black").place(x=530, y=12, width=110, height=30)
        btn_showall = Button(frame2,command=self.fetch_from_db, text="Show All", font=("times new roman", 18, "bold"), bd=2, relief=RAISED,
                           cursor="hand2", bg="black", fg="white", activebackground="white",
                           activeforeground="black").place(x=650, y=12, width=130, height=30)


        frame3 = Frame(frame2, bd=3, relief=RIDGE, bg="light pink")
        frame3.place(x=8, y=60, width=770, height=510)

        scroll_x=Scrollbar(frame3,orient=HORIZONTAL)
        scroll_y=Scrollbar(frame3,orient=VERTICAL)
        self.attendance_table=ttk.Treeview(frame3,column=("regd","name","course","time","date","attendance","id"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("regd",text="Registration No.")
        self.attendance_table.heading("name",text="Student Name")
        self.attendance_table.heading("course",text="Branch")
        self.attendance_table.heading("time",text="Time")
        self.attendance_table.heading("date",text="Date")
        self.attendance_table.heading("attendance", text="Attendance Report")
        self.attendance_table.heading("id",text="Attendance ID")
        self.attendance_table['show']='headings'
        self.attendance_table.column("regd", width=150)
        self.attendance_table.column("name", width=170)
        self.attendance_table.column("course", width=150)
        self.attendance_table.column("time", width=150)
        self.attendance_table.column("date", width=150)
        self.attendance_table.column("attendance", width=150)
        self.attendance_table.column("id", width=150)
        self.attendance_table.pack(fill=BOTH,expand=1)
        self.fetch_from_db()
        self.attendance_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.attendance_table.bind("<ButtonRelease-1>",self.db_get_cursor)

        #=================Fetch Data========================================
    def fetch_from_db(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
            cur=con.cursor()
            cur.execute("select * from `attendance`")
            rows=cur.fetchall()
            self.attendance_table.delete(*self.attendance_table.get_children())
            for row in rows:
                self.attendance_table.insert('',END,values=row)
            con.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def fetch_data_from_file(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)
    
    #============import csv=======================
    def import_csv(self):
        global my_data
        my_data.clear()
        self.clear_table()
        file_open=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV file",filetype=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with open(file_open) as myfile:
            csvread=csv.reader(myfile,delimiter=',')
            for i in csvread:
                my_data.append(i)
            self.fetch_data_from_file(my_data)

    #============export csv=======================
    def export_csv(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("Error","No data found in table !",parent=self.root)
                return False
            file_open=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV file",filetype=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
            with open(file_open,mode="w",newline="") as myfile:
                export_write=csv.writer(myfile,delimiter=",")
                for i in my_data:
                    export_write.writerow(i)
                messagebox.showinfo("Success","Your data has exported as " +os.path.basename(file_open)+ " Successfully !!",parent=self.root)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def get_cursor(self,ev):
        cursor_row=self.attendance_table.focus()
        contents=self.attendance_table.item(cursor_row)
        row=contents['values']
        self.regd_var.set(row[0])
        self.name_var.set(row[1])
        self.branch_var.set(row[2])
        self.time_var.set(row[3])
        self.date_var.set(row[4])
        self.status_var.set(row[5])

    def db_get_cursor(self,ev):
        cursor_row=self.attendance_table.focus()
        contents=self.attendance_table.item(cursor_row)
        row=contents['values']
        self.regd_var.set(row[0])
        self.name_var.set(row[1])
        self.branch_var.set(row[2])
        self.time_var.set(row[3])
        self.date_var.set(row[4])
        self.status_var.set(row[5])
        self.id_var.set(row[6])


    def clear_table(self):
        self.id_var.set("")
        self.regd_var.set("")
        self.name_var.set("")
        self.branch_var.set("")
        self.time_var.set("")
        self.date_var.set("")
        self.status_var.set("select")
        self.search_by_var.set("Select Option")
        self.search_txt_var.set("")
        self.fetch_from_db()

    def add_attendance(self):
        if self.regd_var.get()=="" or self.status_var.get()=="":
            messagebox.showerror("Error","All fields are required ?",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("select * from attendance where `Attendance ID`=%s",(self.id_var.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Attendance ID is Available\nTry with another",parent=self.root)
                else:
                    con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                    cur=con.cursor()
                    cur.execute("INSERT INTO `attendance` VALUES (%s,%s,%s,%s,%s,%s,%s)",(
                            self.regd_var.get(),
                            self.name_var.get(),
                            self.branch_var.get(),
                            self.time_var.get(),
                            self.date_var.get(),
                            self.status_var.get(),
                            self.id_var.get()
                            )
                            )
                    con.commit()
                    self.clear_table()
                    con.close()
                    messagebox.showinfo("Success","Attendance added Successfully !!",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
 
    def delete_attendance(self):
        if self.regd_var.get()=="":
            messagebox.showerror("Error","All fields are required ?",parent=self.root)
        else:
            ask=messagebox.askyesno("DELETE","Do you want to delete the data ?",parent=self.root)
            if ask > 0:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("DELETE FROM `attendance` WHERE `Attendance ID`=%s",(self.id_var.get()))
                con.commit()
                self.clear_table()
                con.close()
                messagebox.showinfo("Success","Attendance deleted Successfully !!",parent=self.root)
                
    def update_attendance(self):
        if self.regd_var.get()=="" or self.status_var.get()=="Select":
            messagebox.showerror("Error","All fields are required ?",parent=self.root)
        else:
            ask=messagebox.askyesno("DELETE","Do you want to update the data ?",parent=self.root)
            if ask > 0:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("UPDATE `attendance` SET `Regd. No.`=%s,`Name`=%s,`Branch`=%s,`Time`=%s,`Date`=%s,`Status`=%s WHERE `Attendance ID`=%s",(
                    self.regd_var.get(),
                    self.name_var.get(),
                    self.branch_var.get(),
                    self.time_var.get(),
                    self.date_var.get(),
                    self.status_var.get(),
                    self.id_var.get()
                    )
                    )
                con.commit()
                self.clear_table()
                con.close()
                messagebox.showinfo("Success","Data updated Successfully",parent=self.root)

    def search_data(self):
        if self.search_by_var.get()=="Select Option":
            messagebox.showerror("Error","Please select the search type ?",parent=self.root)
        elif self.search_txt_var.get()=="":
            messagebox.showerror("Error","Search field must be filled as per the search type !!",parent=self.root)
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
            cur=con.cursor()
            cur.execute("select * from `attendance` where"+str(self.search_by_var.get())+" LIKE '%"+str(self.search_txt_var.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.attendance_table.delete(*self.attendance_table.get_children())
                for row in rows:
                    self.attendance_table.insert("",END,values=row)
            con.commit()
            con.close()    


if __name__ =='__main__':
    root=Tk()
    object=attendance(root)
    root.mainloop()