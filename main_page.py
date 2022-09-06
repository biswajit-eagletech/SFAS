from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import os
from student import all_student_details
from attendance_window import attendance
from training import train_data
from change_pass import change_window 
from face_rec import face_recgnition
from developer import developer

class main_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Student With Face Detection Attendance Management System")
        self.root.geometry("1280x650+0+0")
        self.root.config(bg="black")
        self.root.iconbitmap("images/face1.1.ico")
        self.root.grab_set()
        self.root.focus_force()
        self.root.resizable(0,0)

        #=======================Upper Images==========================
        img1=Image.open(r"images\img19.jpeg")
        img1=img1.resize((315,90),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img1)
        img_lbl1=Label(self.root,image=self.img1).place(x=0,y=0)

        img2=Image.open(r"images\img2.png")
        img2=img2.resize((320,90),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(img2)
        img_lbl2=Label(self.root,image=self.img2).place(x=315,y=0)

        #=======================All Images==========================
        img3=Image.open(r"images\img4.png")
        img3=img3.resize((320,90),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(img3)
        img_lbl3=Label(self.root,image=self.img3).place(x=635,y=0)

        img4=Image.open(r"images\img20.webp")
        img4=img4.resize((325,90),Image.ANTIALIAS)
        self.img4=ImageTk.PhotoImage(img4)
        img_lbl4=Label(self.root,image=self.img4).place(x=950,y=0)

        #=======================Upper Images==========================
        main=Image.open(r"images\mainlogo.jpg")
        main=main.resize((60,50),Image.ANTIALIAS)
        self.main=ImageTk.PhotoImage(main)
        # img_main=Label(self.root,image=self.main).place(x=0,y=0)
        title=Label(self.root,text="Student Management And Facial Attendance System",image=self.main,compound=LEFT,anchor=W,font=("goudy old style",37,"bold"),bg="#262626",fg="cyan",bd=3,relief=RAISED).place(x=0,y=93,relwidth=1)

        #=======================Bottom Images==========================
        img5=Image.open(r"images\img3.png")
        img5=img5.resize((1280,490),Image.ANTIALIAS)
        self.img5=ImageTk.PhotoImage(img5)
        img_lbl5=Label(self.root,image=self.img5).place(x=0,y=160)

        #=======All Buttons======================================
        #=========Buttons images=================================
        #===========row 1======================
        img6=Image.open(r"images\student1.jpg")
        img6=img6.resize((200,170),Image.ANTIALIAS)
        self.img6=ImageTk.PhotoImage(img6)

        img7=Image.open(r"images\facedetect.png")
        img7=img7.resize((200,170),Image.ANTIALIAS)
        self.img7=ImageTk.PhotoImage(img7)
        
        img8=Image.open(r"images\attendance.png")
        img8=img8.resize((200,170),Image.ANTIALIAS)
        self.img8=ImageTk.PhotoImage(img8)

        img9=Image.open(r"images\img13.png")
        img9=img9.resize((230,170),Image.ANTIALIAS)
        self.img9=ImageTk.PhotoImage(img9)
        
        #===========row 1======================
        img10=Image.open(r"images\train.png")
        img10=img10.resize((200,170),Image.ANTIALIAS)
        self.img10=ImageTk.PhotoImage(img10)

        img11=Image.open(r"images\photos.png")
        img11=img11.resize((200,170),Image.ANTIALIAS)
        self.img11=ImageTk.PhotoImage(img11)
        
        img12=Image.open(r"images\dev.jpg")
        img12=img12.resize((200,170),Image.ANTIALIAS)
        self.img12=ImageTk.PhotoImage(img12)

        img13=Image.open(r"images\exit.jpg")
        img13=img13.resize((200,200),Image.ANTIALIAS)
        self.img13=ImageTk.PhotoImage(img13)
        
        #===========row 1======================
        btn1=Button(self.root,command=self.add_students,text="Student Management",font=("times new roman",15,"bold"),compound=TOP,bg="black",fg="white",bd=2,relief=RIDGE,image=self.img6,cursor="hand2").place(x=45,y=180,width=200,height=200)
        btn2=Button(self.root,command=self.face_recgonition,text="Face Recognizer",font=("times new roman",16,"bold"),compound=TOP,bg="black",fg="white",bd=2,relief=RIDGE,image=self.img10,cursor="hand2").place(x=375,y=180,width=200,height=200)
        btn3=Button(self.root,command=self.student_attendance,text="Attendance",font=("times new roman",16,"bold"),compound=TOP,bg="black",fg="white",bd=2,relief=RIDGE,image=self.img8,cursor="hand2").place(x=705,y=180,width=200,height=200)
        btn4=Button(self.root,command=self.change_password,text="Change Password",font=("times new roman",16,"bold"),compound=TOP,bg="black",fg="white",bd=2,relief=RIDGE,image=self.img9,cursor="hand2").place(x=1035,y=180,width=200,height=200)

        
        #===========row 2======================
        btn5=Button(self.root,command=self.student_train_data,text="Train Data",font=("times new roman",16,"bold"),compound=TOP,bg="black",fg="white",bd=2,relief=RIDGE,image=self.img7,cursor="hand2").place(x=45,y=415,width=200,height=200)
        btn6=Button(self.root,command=self.open_image,text="All Photos",font=("times new roman",16,"bold"),compound=TOP,bg="black",fg="white",bd=2,relief=RIDGE,image=self.img11,cursor="hand2").place(x=375,y=415,width=200,height=200)
        btn7=Button(self.root,command=self.developer,text="Developer",font=("times new roman",16,"bold"),compound=TOP,bg="black",fg="white",bd=2,relief=RIDGE,image=self.img12,cursor="hand2").place(x=705,y=415,width=200,height=200)
        btn8=Button(self.root,command=self.exit,fg="gold",bd=2,relief=RIDGE,image=self.img13,cursor="hand2").place(x=1035,y=415,width=200,height=200)


    def add_students(self):
        self.new_window=Toplevel(self.root)
        self.app=all_student_details(self.new_window)

    def student_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)

    def student_train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train_data(self.new_window)

    def face_recgonition(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recgnition(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)

    def change_password(self):
        self.new_window=Toplevel(self.root)
        self.app=change_window(self.new_window)


    def open_image(self):
        os.startfile("cap_images")
    def exit(self):
        ask = messagebox.askyesno("EXIT","Do you want to Exit ?",parent=self.root)
        if ask == True:
            self.root.destroy()

if __name__ =='__main__':
    root=Tk()
    object=main_page(root)
    root.mainloop()