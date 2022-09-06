from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
from add_students import student
from manage_student import mang_student
from stu_sub_info import miscellenious

class all_student_details:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1280x650+0+0")
        self.root.focus_force()
        self.root.grab_set()
        self.root.iconbitmap("images/icon1.ico")
        self.root.resizable(0,0)

        #=========frame1========================
        frame1=Frame(self.root,bg="snow",bd=1,relief=RIDGE)
        frame1.place(x=215,y=5,width=1060,height=80)

        img1=Image.open(r"images\add-student.png")
        img1=img1.resize((60,50),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img1)

        lbl_title=Label(frame1,text=" STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),image=self.img1,compound=LEFT,bg="snow",fg="salmon").place(x=20,y=10)
        
        hr=Label(frame1,bg="black").place(x=85,y=60,width=700,height=1)
        
        #=========frame2========================
        frame2=Frame(self.root,bg="snow",bd=1,relief=RIDGE)
        frame2.place(x=7,y=5,width=200,height=1260)

        btn1=Button(frame2,command=self.student_window,text="Add Student ",font=("times new roman",10,"bold"),bg="snow",fg="black",bd=1,relief=GROOVE,cursor="hand2",activebackground="snow",activeforeground="black").place(x=6,y=220,width=185,height=40)
        btn2=Button(frame2,command=self.mang_student_window,text="Manage Student",font=("times new roman",10,"bold"),bg="snow",fg="black",bd=1,relief=GROOVE,cursor="hand2",activebackground="snow",activeforeground="black").place(x=6,y=275,width=185,height=40)
        btn3=Button(frame2,command=self.info_sub_student_window,text="Miscellaneous",font=("times new roman",10,"bold"),bg="snow",fg="black",bd=1,relief=GROOVE,cursor="hand2",activebackground="snow",activeforeground="black").place(x=6,y=330,width=185,height=40)
        
        #=======================Upper Images==========================
        img2=Image.open(r"images\studentbg.jpeg")
        img2=img2.resize((1065,565),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(img2)
        img_lbl2=Label(self.root,image=self.img2).place(x=210,y=85)

        img3=Image.open(r"images\add_student.ico")
        img3=img3.resize((180,180),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(img3)
        img_lbl3=Label(self.root,image=self.img3,bg="snow").place(x=15,y=15)

        img4=Image.open(r"images\student1.jpg")
        img4=img4.resize((180,180),Image.ANTIALIAS)
        self.img4=ImageTk.PhotoImage(img4)
        img_lbl4=Label(self.root,image=self.img4,bg="snow").place(x=15,y=395)

    def student_window(self):
        self.newWindow = Toplevel(self.root)
        self.app = student(self.newWindow)

    def mang_student_window(self):
        self.newWindow = Toplevel(self.root)
        self.app = mang_student(self.newWindow)
    
    def info_sub_student_window(self):
        self.newWindow = Toplevel(self.root)
        self.app = miscellenious(self.newWindow)



if __name__ == '__main__':
    root=Tk()
    obj=all_student_details(root)
    root.mainloop()