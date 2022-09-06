from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import pymysql

class change_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Chnge Password window")
        self.root.geometry("700x450+300+100")
        self.root.config(bg="white")
        self.root.iconbitmap("images/icon5.ico")
        self.root.grab_set()
        self.root.focus_force()
        self.root.resizable(0,0)

        self.ch_pass_mail_var=StringVar()
        self.ch_old_pass_mail_var=StringVar()
        self.ch_new_pass_mail_var=StringVar()

        #=======================Upper Images==========================
        img1=Image.open(r"images\change1.png")
        img1=img1.resize((230,145),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img1)
        img_lbl1=Label(self.root,image=self.img1,bd=0).place(x=210,y=0)

        ch_mail_lbl=Label(self.root,text="E_mail ID",font=("times new roman",22,"bold"),bg="white",fg="black").place(x=70,y=150)
        ch_mail_txt=Entry(self.root,textvariable=self.ch_pass_mail_var,font=("times new roman",17,"bold"),bg="light yellow",fg="black",bd=2
        ,relief=SUNKEN,width=24).place(x=280,y=151)

        ch_opass_lbl=Label(self.root,text="Old Password",font=("times new roman",22,"bold"),bg="white",fg="black").place(x=70,y=225)
        ch_opass_txt=Entry(self.root,textvariable=self.ch_old_pass_mail_var,font=("times new roman",17,"bold"),bg="light yellow",fg="black",bd=2
        ,relief=SUNKEN,width=24).place(x=280,y=225)

        ch_npass_lbl=Label(self.root,text="New Password",font=("times new roman",22,"bold"),bg="white",fg="black").place(x=70,y=300)
        ch_npass_txt=Entry(self.root,textvariable=self.ch_new_pass_mail_var,font=("times new roman",17,"bold"),bg="light yellow",fg="black",bd=2
        ,relief=SUNKEN,width=24).place(x=280,y=300)

        ch_pass_btn=Button(self.root,command=self.change,text="Change Password",font=("times new roman",20,"bold"),cursor="hand2",bd=0,bg="green",fg="white"
        ,activebackground="white",activeforeground="green",width=16).place(x=200,y=365,height=45)
        
        ch_clear_btn=Button(self.root,command=self.change_clear,text="Clear",font=("times new roman",20,"bold"),cursor="hand2",bd=0,bg="peru",fg="white"
        ,activebackground="white",activeforeground="peru",width=11).place(x=485,y=365,height=45)

    def change(self):
        if self.ch_pass_mail_var.get()=="" or self.ch_old_pass_mail_var.get()=="":
            messagebox.showerror("Error","Please All Fields Are required ?",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("SELECT * FROM `register` WHERE `Email`=%s and `Password`=%s",(self.ch_pass_mail_var.get(), self.ch_old_pass_mail_var.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email Address or Password !",parent=self.root)
                else:
                    cur.execute("UPDATE `register` SET `Password`=%s WHERE `Email`=%s ",(self.ch_new_pass_mail_var.get(),self.ch_pass_mail_var.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success",f"Your Password has been Reset\nPlease Login with new Password\nAnd your Password is  {self.ch_new_pass_mail_var.get()}",parent=self.root)                
                    self.change_clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)


    def change_clear(self):
        self.ch_pass_mail_var.set("")
        self.ch_old_pass_mail_var.set("")
        self.ch_new_pass_mail_var.set("")


if __name__ == '__main__':
    root=Tk()
    object=change_window(root)
    root.mainloop()