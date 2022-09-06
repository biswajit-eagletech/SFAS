from tkinter import*
from tkinter import ttk,messagebox
import pymysql
from PIL import ImageTk,Image


class Register():
    def __init__(self,root):
        self.root=root
        self.root.title("Register New Employee Window")
        self.root.geometry("1280x650+0+0")
        self.root.iconbitmap("images/icon8.ico")
        self.root.resizable(0,0)

        #======================Images==========================
        img1=Image.open(r"images\register2.png")
        img1=img1.resize((1280,660),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img1)
        img_lbl1=Label(self.root,image=self.img1,bd=0).place(x=0,y=0)

        #======Register Frame===============
        reg_frame=Frame(self.root,bg="white",bd=0,relief=RIDGE)
        reg_frame.place(x=450,y=100,width=650,height=450)
        
        title=Label(reg_frame,text="REGISTER HERE",font=("times new roman",25,"bold"),bg="white",fg="green").place(x=60,y=20)

#==============Row1=====================================
        fname_lbl=Label(reg_frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=40,y=80)
        self.fname_txt=Entry(reg_frame,font=("times new roman",13),bd=2,relief=SUNKEN,bg="light yellow",fg="black",width=20)
        self.fname_txt.place(x=40,y=110)

        lname_lbl=Label(reg_frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=80)
        self.lname_txt=Entry(reg_frame,font=("times new roman",13),bd=2,relief=SUNKEN,bg="light yellow",fg="black",width=20)
        self.lname_txt.place(x=370,y=110)

#==============Row2=====================================
        con_lbl=Label(reg_frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=40,y=150)
        self.con_txt=Entry(reg_frame,font=("times new roman",13),bd=2,relief=SUNKEN,bg="light yellow",fg="black",width=20)
        self.con_txt.place(x=40,y=180)

        email_lbl=Label(reg_frame,text="E_mail Id",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=150)
        self.email_txt=Entry(reg_frame,font=("times new roman",13),bd=2,relief=SUNKEN,bg="light yellow",fg="black",width=20)
        self.email_txt.place(x=370,y=180)

#==============Row3=====================================
        s_ques_lbl=Label(reg_frame,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        s_ques_lbl.place(x=40,y=220)
        self.s_ques_com=ttk.Combobox(reg_frame,font=("times new roman",13),width=18,state="readonly",justify="center")
        self.s_ques_com['values']=("Selcet","Your Pet Name","Best Friend Name","Date of Birth","Your Cognent")
        self.s_ques_com.current(0)
        self.s_ques_com.place(x=40,y=250)

        answer_lbl=Label(reg_frame,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=220)
        self.answer_txt=Entry(reg_frame,font=("times new roman",13),bd=2,relief=SUNKEN,bg="light yellow",fg="black",width=20)
        self.answer_txt.place(x=370,y=250)

#==============Row2=====================================
        pass_lbl=Label(reg_frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=40,y=290)
        self.pass_txt=Entry(reg_frame,font=("times new roman",13),bd=2,relief=SUNKEN,bg="light yellow",fg="black",width=20)
        self.pass_txt.place(x=40,y=320)

        c_pass_lbl=Label(reg_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        c_pass_lbl.place(x=370,y=290)
        self.c_pass_txt=Entry(reg_frame,font=("times new roman",13),bd=2,relief=SUNKEN,bg="light yellow",fg="black",width=20)
        self.c_pass_txt.place(x=370,y=320)
        
        self.var_chk=IntVar()
        chk_btn=Checkbutton(reg_frame,text="I Agree to the Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0
        ,font=("times new roman",11,"bold"),bg="white",fg="black",activebackground="white",cursor="hand2").place(x=40,y=355)
        
        reg_btn=Button(reg_frame,command=self.register_data,text="Register Now ➡",font=("times new roman",16,"bold")
        ,bd=0,bg="green",fg="white",activebackground="white",activeforeground="green",width=20,cursor="hand2").place(x=40,y=390)

        clr_btn=Button(reg_frame,command=self.clear,text="Clear",font=("times new roman",16,"bold")
        ,bd=0,bg="red",fg="white",activebackground="white",activeforeground="red",width=15,cursor="hand2").place(x=370,y=390)

        sign_frame=Frame(self.root,bg="#262626",bd=0,relief=RIDGE)
        sign_frame.place(x=150,y=100,width=300,height=450)
        
        #======================Images==========================
        img2=Image.open(r"images\socialimpact1-2.png")
        img2=img2.resize((300,350),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(img2)
        img_lbl2=Label(sign_frame,image=self.img2,bd=0).place(x=0,y=46)

        sign_btn=Button(sign_frame,command=self.signin_window,text="Sign In",font=("times new roman",15,"bold"),bd=0
        ,bg="white",fg="#262626",activebackground="#262626",activeforeground="white",width=15,cursor="hand2").place(x=55,y=405)
#=======================
        lbl0=Label(sign_frame,text="SOCIAL IMPACT",font=("times new roman",20,"bold"),bg="#262626",fg="white").place(x=30,y=5)
#=======================                

#===============Database Workings==================================               
    def register_data(self):
        if self.fname_txt.get()=="" or self.con_txt.get()=="" or self.email_txt.get()=="" or self.s_ques_com.get()==""or self.answer_txt.get()=="" or self.pass_txt.get()=="" or self.c_pass_txt.get()=="":
            messagebox.showerror("Error","All fields are required!!!",parent=self.root)
        elif self.pass_txt.get() != self.c_pass_txt.get():
            messagebox.showerror("Error","Password and Confirm Password Must Same!!",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms and Conditions",parent=self.root)
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")                                
            cur=con.cursor()
            cur.execute("select * from register where Email=%s",self.email_txt.get())
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exist\nPlease try with another Email !!!",parent=self.root)
            else:

                cur.execute("insert into register(`First Name`,`Last Name`,`Contact`,`Email`,`S Question`,`Answer`,`Password`)values(%s,%s,%s,%s,%s,%s,%s)",
                                                            (self.fname_txt.get(),
                                                            self.lname_txt.get(),
                                                            self.con_txt.get(),
                                                            self.email_txt.get(),
                                                            self.s_ques_com.get(),
                                                            self.answer_txt.get(),
                                                            self.pass_txt.get()
                                                            ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Registration Successful !",parent=self.root)  
                self.clear()     

    def clear(self):
        self.fname_txt.delete(0,END)
        self.lname_txt.delete(0,END)           
        self.con_txt.delete(0,END)           
        self.email_txt.delete(0,END)           
        self.answer_txt.delete(0,END)           
        self.pass_txt.delete(0,END)           
        self.c_pass_txt.delete(0,END)           
        self.s_ques_com.current(0)
        self.var_chk.set(0)

    def signin_window(self):
        self.root.destroy()

    



if __name__ == '__main__':
    root=Tk()
    obj=Register(root)
    root.mainloop()