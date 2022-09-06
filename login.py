from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import pymysql
from main_page import main_page 
from register import Register



class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Employee Window")
        self.root.geometry("1280x650+0+0")
        self.root.iconbitmap("images/icon6.ico")
        self.root.resizable(0,0)
        bg_color="#caf0f9"

        #=======================Images==========================
        img1 = Image.open("images\login1.jpg")
        img1 = img1.resize((1280, 665), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(img1)
        img_lbl1 = Label(self.root, image=self.img1,bd=0).place(x=0, y=0)
        #==============================================
        img2 = Image.open("images\log1.png")
        img2 = img2.resize((30, 25), Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(img2)
        #=============================================
        img3 = Image.open("images\pass2.png")
        img3 = img3.resize((30, 25), Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(img3)

        #========Frame 1================================
        frame1=Frame(self.root,bd=3,relief=RIDGE,bg="#caf0f9")
        frame1.place(x=120,y=100,width=350,height=390)

        login_lbl=Label(frame1,text="LOGIN HERE",font=("elephant",23,"bold"),bg=bg_color,fg="#262626").place(x=0,y=20,relwidth=1)

        user_lbl=Label(frame1,text="Username",font=("Andalus",18,"bold"),image=self.img2,compound=LEFT,bg=bg_color,fg="#767171").place(x=40,y=80)
        self.user_txt=Entry(frame1,font=("times new roman",18),bd=2,relief=SUNKEN,bg="white",fg="black")
        self.user_txt.place(x=40,y=120,width=250,height=32)

        pass_lbl=Label(frame1,text="Password",font=("Andalus",18,"bold"),image=self.img3,compound=LEFT,bg=bg_color,fg="#767171").place(x=40,y=165)
        self.pass_txt=Entry(frame1,font=("times new roman",18),show="*",bd=2,relief=SUNKEN,bg="white",fg="black")
        self.pass_txt.place(x=40,y=205,width=250,height=32)


        btn_login=Button(frame1,command=self.login,text="Log In",font=("Arial Rounded MT Bold",17),bd=2,relief=RAISED,bg="#00B0F0",fg="white",activebackground="white",activeforeground="#00B0F0",cursor="hand2").place(x=84,y=260,width=160,height=35)

        line=Label(frame1,bg='#132028').place(x=30,y=320,width=270,height=1)
        or_lbl=Label(frame1,text="OR",font=("times new roman",15),bg=bg_color,fg="purple").place(x=145,y=307)

        btn_forgot=Button(frame1,command=self.forget_password_Window,text="Forgot Password ?",font=("times new roman",13,"bold"),bd=0,bg=bg_color,fg="#00759E",activebackground=bg_color,activeforeground="#00759E",cursor="hand2").place(x=80,y=345,width=170,height=25)

        #=======Frame 2================================
        frame2 = Frame(self.root, bd=3, relief=RIDGE, bg="#caf0f9")
        frame2.place(x=120, y=510, width=350, height=60)

        sign_lbl=Label(frame2,text="Don't have an account ?",font=("times new roman",13),bg=bg_color,fg="black").place(x=50,y=15)
        btn_sign=Button(frame2,command=self.sign_up,text="Sign Up",font=("times new roman",13,"bold"),bd=0,bg=bg_color,fg="#00759E",activebackground=bg_color,activeforeground="#00759E",cursor="hand2").place(x=220,y=13)


#============================================================================================================================================================================================================================================================
    def login(self):
        if self.user_txt.get()=="" or self.pass_txt.get()=="":
            messagebox.showerror("Error","All fields are required ?",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("SELECT * FROM `register` WHERE `Email`=%s and `Password`=%s",(self.user_txt.get(), self.pass_txt.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email Address or Password !",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome {self.user_txt.get()} ",parent=self.root)
                    self.new_window=Toplevel(self.root)
                    self.app=main_page(self.new_window)
                    self.clear_log1()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    
    #==================================forget_password_Window function=====================================================================
    def forget_password_Window(self):
        if self.user_txt.get()=="":
            messagebox.showerror("Error","Enter your Email Id to reset your Password ?",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("SELECT * FROM `register` WHERE `Email`=%s",self.user_txt.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter your valid Email Id\nto reset your Password ?",parent=self.root)
                else:
                    con.close()
                    #===========Forgot Window=========================
                    self.root2=Toplevel()
                    self.root2.title("Forget Password Window")
                    self.root2.geometry("320x400+500+150")
                    self.root2.config(bg="white")
                    self.root2.resizable(False,False)
                    self.root2.focus_force()
                    self.root2.grab_set()
                    self.root2.iconbitmap("images/icon7.ico")

                    title=Label(self.root2,text="Forget Password",font=("times new roman",25,"bold"),bg="white",fg="red").place(x=0,y=20,relwidth=1)

                    s_ques_lbl=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=45,y=90)
                    self.s_ques_com=ttk.Combobox(self.root2,font=("times new roman",13),width=23,state="readonly",justify="center")
                    self.s_ques_com['values']=("Selcet","Your Pet Name","Best Friend Name","Date of Birth","Your Cognent")
                    self.s_ques_com.current(0)
                    self.s_ques_com.place(x=45,y=120)

                    answer_lbl=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=45,y=160)
                    self.answer_txt=Entry(self.root2,font=("times new roman",13),bd=1,relief=SUNKEN,bg="light gray",fg="black",width=25)
                    self.answer_txt.place(x=45,y=190)

                    new_pass_lbl=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                    new_pass_lbl.place(x=45,y=230)
                    self.new_pass_txt=Entry(self.root2,font=("times new roman",13),bd=1,relief=SUNKEN,bg="light gray",fg="black",width=25)
                    self.new_pass_txt.place(x=45,y=270)

                    res_pass_btn=Button(self.root2,command=self.forget_password,text="Reset Password",font=("times new roman",15,"bold")
                    ,bd=0,bg="green",fg="white",activebackground="white",activeforeground="green",width=15,cursor="hand2").place(x=65,y=320)
        #=====================================================================================================#
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    
    #==================Forget to Reset Functionality===========================================================
    def forget_password(self):
        if self.s_ques_com.get()=="Select" or self.answer_txt.get()=="" or self.new_pass_txt.get()=="":
            messagebox.showerror("Error","All fields are required ?",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("SELECT * FROM `register` WHERE `Email`=%s and `S Question`=%s and `Answer`=%s",(self.user_txt.get()
                ,self.s_ques_com.get(),self.answer_txt.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select correct Security Question / Answer ?",parent=self.root2)
                else:
                    cur.execute("UPDATE `register` SET `Password`=%s WHERE `Email`=%s ",(self.new_pass_txt.get(),self.user_txt.get()))
                    con.commit()
                    messagebox.showinfo("Success",f"Your Password has been Reset.\nPlease Login with new Password.\nAnd your new Password is  {self.new_pass_txt.get()}",parent=self.root2)                
                    self.root2.destroy()
                    self.clear_log()
                con.close()
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)


    def clear_log(self):
        self.user_txt.delete(0,END)
        self.pass_txt.delete(0,END)
        self.s_ques_com.set("Select")
        self.answer_txt.delete(0,END) 
        self.new_pass_txt.delete(0,END)

    def clear_log1(self):
        self.user_txt.delete(0,END)
        self.pass_txt.delete(0,END)

    def sign_up(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)



if __name__ == '__main__':
    root=Tk()
    obj=login(root)
    root.mainloop()