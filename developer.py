from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import webbrowser



class developer:
    def __init__(self,root):
        self.root = root
        self.root.title("About developer")
        self.root.geometry("1280x650+0+0")
        self.root.grab_set()
        self.root.focus_force()
        self.root.iconbitmap("images\devlop.ico")
        self.root.resizable(0,0)
        self.root.config(bg="white")

        title=Label(self.root,text="About Developers",font=("goudy old style",30,"bold"),bg="black",fg="peru").place(x=0,y=0,relwidth=1)

         #====facebook============================
        img1_1=Image.open(r"images\facebook.png")
        img1_1=img1_1.resize((35,30),Image.ANTIALIAS)
        self.img1_1=ImageTk.PhotoImage(img1_1)
        #=======instagram========================
        img1_2=Image.open(r"images\instagram.png")
        img1_2=img1_2.resize((35,30),Image.ANTIALIAS)
        self.img1_2=ImageTk.PhotoImage(img1_2)
        #=======mail========================
        img_mail_1=Image.open(r"images\mail1.webp")
        img_mail_1=img_mail_1.resize((35,30),Image.ANTIALIAS)
        self.img_mail_1=ImageTk.PhotoImage(img_mail_1)
    

        # img1_photo1=Image.open(r"images\smruti.jpeg")
        # img1_photo1=img1_photo1.resize((345,600),Image.ANTIALIAS)
        # self.img1_photo1=ImageTk.PhotoImage(img1_photo1)
        # img_photo_lbl1=Label(self.root,image=self.img1_photo1,bd=0).place(x=935,y=52)


        # name_lbl=Label(self.root,text="Name : Smruti Ranjan Kabi",font=("times new roman",23,"bold"),fg="#212121",bg="white").place(x=20,y=60)
        # regd_lbl=Label(self.root,text="Regd. no : 1701335040",font=("times new roman",23,"bold"),fg="#212121",bg="white").place(x=20,y=110)
        # branch_lbl=Label(self.root,text="Branch : CSE",font=("times new roman",23,"bold"),fg="#212121",bg="white").place(x=20,y=160)
        # sem_lbl=Label(self.root,text="Sem : 8th",font=("times new roman",23,"bold"),fg="#212121",bg="white").place(x=20,y=210)
        # mail_lbl=Label(self.root,text=" : smrutiranjank@eagletech.in",image=self.img_mail_1,compound=LEFT,font=("times new roman",17,"bold"),fg="#212121",bg="white").place(x=20,y=260)

        # face_lbl_1=Button(self.root,image=self.img1_1,compound=LEFT,cursor="hand2",font=("times new roman",20,"bold"),fg="white",bg="white").place(x=15,y=215)
        # face_lbl1=Label(self.root,text=": https://www.facebook.com/soumyaranjanseth.gudu",font=("times new roman",13),fg="white",bg="black").place(x=60,y=220)
        
        # insta_lbl_1=Button(self.root,image=self.img1_2,compound=LEFT,cursor="hand2",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=255)
        # insta_lbl1=Label(self.root,text=": https://instagram.com/mr._mind___blowing?igshid=1wv0wnywks8gi",font=("times new roman",9),fg="white",bg="black").place(x=58,y=262)




if __name__ == '__main__':
    root=Tk()
    object=developer(root)
    root.mainloop()