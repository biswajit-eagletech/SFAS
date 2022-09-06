from tkinter import *
from tkinter import ttk,messagebox
import pymysql

class miscellenious:
    def __init__(self,root):
        self.root=root
        self.root.title("Miscellaneous")
        self.root.geometry("1055x525+215+120")
        self.root.resizable(0,0)
        self.root.focus_force()
        self.root.grab_set()
        self.root.iconbitmap("images/icon1.ico")

        
        title=Label(self.root,text="Miscellenaous",font=("times new roman",35,"bold"),bg="plum",fg="black",bd=5,relief=RAISED).place(x=0,y=4,relwidth=1,height=67)

        frame1=Frame(self.root,bd=3,relief=RIDGE,bg="yellow")
        frame1.place(x=2,y=75,relwidth=1,height=220)

        course_code_lbl=Label(frame1,text="Course Code",font=("times new roman",20,"bold"),bg="yellow",fg="black").place(x=20,y=40)
        self.course_code_txt=Entry(frame1,font=("times new roman",16,"bold"),bg="light yellow",fg="black",bd=3,relief=SUNKEN)
        self.course_code_txt.place(x=220,y=42,width=260,height=30)

        course_name_lbl=Label(frame1,text="Course Name",font=("times new roman",20,"bold"),bg="yellow",fg="black").place(x=20,y=110)
        self.course_name_txt=Entry(frame1,font=("times new roman",16,"bold"),bg="light yellow",fg="black",bd=3,relief=SUNKEN)
        self.course_name_txt.place(x=220,y=110,width=260,height=30)

        btn_add1=Button(frame1,command=self.add_course,text="Add",font=("times new roman",18,"bold"),bg="light green",fg="black",cursor="hand2").place(x=10,y=170,width=180,height=30)        
        btn_update1=Button(frame1,command=self.update_course,text="Update",font=("times new roman",18,"bold"),bg="orange",fg="black",cursor="hand2").place(x=200,y=170,width=180,height=30)        
        btn_delete1=Button(frame1,command=self.delete_course,text="Delete",font=("times new roman",18,"bold"),bg="salmon",fg="black",cursor="hand2").place(x=390,y=170,width=180,height=30)        
        btn_reset1=Button(frame1,command=self.reset_course,text="Reset",font=("times new roman",18,"bold"),bg="purple",fg="black",cursor="hand2").place(x=580,y=170,width=180,height=30)        
        
        course_table_frame=Frame(frame1,bd=3,relief=RIDGE)
        course_table_frame.place(x=770,y=5,width=270,height=205)

        scroll_x=Scrollbar(course_table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(course_table_frame,orient=VERTICAL)
        self.course_table=ttk.Treeview(course_table_frame,column=("code","name"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.course_table.xview)
        scroll_y.config(command=self.course_table.yview)

        self.course_table.heading("code",text="Course Code")
        self.course_table.heading("name",text="Course Name")
        self.course_table['show']='headings'
        self.course_table.column("code",width=150)
        self.course_table.column("name",width=150)
        self.course_table.pack(fill=BOTH,expand=1)
        self.course_table.pack()
        self.course_fetch_data()
        self.course_table.bind("<ButtonRelease-1>",self.course_get_cursor)
        
        #===========================================
        frame2=Frame(self.root,bd=3,relief=RIDGE,bg="red")
        frame2.place(x=2,y=300,relwidth=1,height=220)
        
        branch_code_lbl=Label(frame2,text="Branch Code",font=("times new roman",20,"bold"),bg="red",fg="black").place(x=20,y=40)
        self.branch_code_txt=Entry(frame2,font=("times new roman",16,"bold"),bg="light yellow",fg="black",bd=3,relief=SUNKEN)
        self.branch_code_txt.place(x=220,y=42,width=260,height=30)

        branch_name_lbl=Label(frame2,text="Branch Name",font=("times new roman",20,"bold"),bg="red",fg="black").place(x=20,y=110)
        self.branch_name_txt=Entry(frame2,font=("times new roman",16,"bold"),bg="light yellow",fg="black",bd=3,relief=SUNKEN)
        self.branch_name_txt.place(x=220,y=110,width=260,height=30)

        btn_add2=Button(frame2,command=self.add_branch,text="Add",font=("times new roman",18,"bold"),bg="light green",fg="black",cursor="hand2").place(x=10,y=170,width=180,height=30)        
        btn_update2=Button(frame2,command=self.update_branch,text="Update",font=("times new roman",18,"bold"),bg="orange",fg="black",cursor="hand2").place(x=200,y=170,width=180,height=30)        
        btn_delete2=Button(frame2,command=self.delete_branch,text="Delete",font=("times new roman",18,"bold"),bg="salmon",fg="black",cursor="hand2").place(x=390,y=170,width=180,height=30)        
        btn_reset2=Button(frame2,command=self.reset_branch,text="Reset",font=("times new roman",18,"bold"),bg="purple",fg="black",cursor="hand2").place(x=580,y=170,width=180,height=30)        
        
        branch_table_frame=Frame(frame2,bd=3,relief=RIDGE)
        branch_table_frame.place(x=770,y=5,width=270,height=205)
        
        scroll_x=Scrollbar(branch_table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(branch_table_frame,orient=VERTICAL)
        self.branch_table=ttk.Treeview(branch_table_frame,column=("code","name"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.branch_table.xview)
        scroll_y.config(command=self.branch_table.yview)

        self.branch_table.heading("code",text="Branch Code")
        self.branch_table.heading("name",text="Branch Name")
        self.branch_table['show']='headings'
        self.branch_table.column("code",width=150)
        self.branch_table.column("name",width=150)
        self.branch_table.pack(fill=BOTH,expand=1)
        self.branch_table.pack()
        self.branch_fetch_data()
        self.branch_table.bind("<ButtonRelease-1>",self.branch_get_cursor)
        
        #===============Function=================================================
    
    def add_course(self):
        if self.course_code_txt.get()=="":
            messagebox.showerror("Error","All Fields are required ?",parent=self.root)
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
            cur=con.cursor()
            cur.execute("INSERT INTO `miscelleneous_course` VALUES (%s,%s)",(
                self.course_code_txt.get(),
                self.course_name_txt.get()
                )
                )
            con.commit()
            self.course_fetch_data()
            self.reset_course()
            con.close()
            messagebox.showinfo("Success","Course added Successfully !!",parent=self.root)
    
    def update_course(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
        cur=con.cursor()
        cur.execute("UPDATE `miscelleneous_course` SET `course_name`=%s WHERE `course_code`=%s",(
            self.course_name_txt.get(),
            self.course_code_txt.get()
            )
            )
        con.commit()
        self.course_fetch_data()
        self.reset_course()
        con.close()
        messagebox.showinfo("Success","Course updated Successfully !!",parent=self.root)
    
    def delete_course(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
        cur=con.cursor()
        cur.execute("DELETE FROM `miscelleneous_course` WHERE `course_code`=%s",self.course_code_txt.get())
        con.commit()
        self.reset_course()
        self.course_fetch_data()
        con.close()
        messagebox.showinfo("Success","Course deleted Successfully !!",parent=self.root)

    def reset_course(self):
        self.course_name_txt.delete(0,END)
        self.course_code_txt.delete(0,END) 
        self.course_fetch_data()

    def course_get_cursor(self,ev):
        cursor_row=self.course_table.focus()
        contents=self.course_table.item(cursor_row)
        row=contents['values']
        self.course_code_txt.delete(0,END)        
        self.course_code_txt.insert(END,row[0]) 
        self.course_name_txt.delete(0,END)
        self.course_name_txt.insert(END,row[1])
        
    def course_fetch_data(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
            cur=con.cursor()
            cur.execute("select * from miscelleneous_course")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)
            con.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

#===================================================================================================================================================================================================================================================

    def add_branch(self):
        if self.branch_code_txt.get()=="":
            messagebox.showerror("Error","All Fields are required ?",parent=self.root)
        else:
            try:
                # con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                # cur=con.cursor()
                # cur.execute("select * from add_student where `Adm ID`=%s",(self.branch_code_txt.get()))
                # row=cur.fetchone()
                # if row!=None:
                #     messagebox.showerror("Error","This ID is Available\nTry with another",parent=self.root)
                # else:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("INSERT INTO `miscelleneous_branch` VALUES (%s,%s)",(
                    self.branch_code_txt.get(),
                    self.branch_name_txt.get()
                    )
                    )
                con.commit()
                self.branch_fetch_data()
                self.reset_branch()
                con.close()
                messagebox.showinfo("Success","Branch added Successfully !!",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def update_branch(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
        cur=con.cursor()
        cur.execute("UPDATE `miscelleneous_branch` SET `branch_name`=%s WHERE `branch_code`=%s",(
            self.branch_name_txt.get(),
            self.branch_code_txt.get()
            )
            )
        con.commit()
        self.branch_fetch_data()
        self.reset_branch()
        con.close()
        messagebox.showinfo("Success","Branch updated Successfully !!",parent=self.root)
    
    def delete_branch(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
        cur=con.cursor()
        cur.execute("DELETE FROM `miscelleneous_branch` WHERE `branch_code`=%s",self.branch_code_txt.get())
        con.commit()
        self.branch_fetch_data()
        self.reset_branch()
        con.close()
        messagebox.showinfo("Success","Branch deleted Successfully !!",parent=self.root)

    def reset_branch(self):
        self.branch_name_txt.delete(0,END)
        self.branch_code_txt.delete(0,END) 
        self.branch_fetch_data()       

    def branch_get_cursor(self,ev):
        cursor_row=self.branch_table.focus()
        contents=self.branch_table.item(cursor_row)
        row=contents['values']
        self.branch_code_txt.delete(0,END)        
        self.branch_code_txt.insert(END,row[0]) 
        self.branch_name_txt.delete(0,END)
        self.branch_name_txt.insert(END,row[1])
        
    def branch_fetch_data(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
            cur=con.cursor()
            cur.execute("select * from miscelleneous_branch")
            rows=cur.fetchall()
            self.branch_table.delete(*self.branch_table.get_children())
            for row in rows:
                self.branch_table.insert('',END,values=row)
            con.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    object=miscellenious(root)
    root.mainloop()