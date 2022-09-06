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

        title=Label(self.root,text="About Developers",font=("goudy old style",30,"bold"),bg="black",fg="peru").place(x=0,y=0,relwidth=1)

        #=======================frame1================================================================
        frame1=Frame(self.root,bg="black",bd=3,relief=RIDGE)
        frame1.place(x=0,y=50,width=640,height=300)
        #=======================Images==========================
        img1=Image.open(r"images\dev5.jpg")
        img1=img1.resize((640,300),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img1)
        img_lbl1=Label(frame1,image=self.img1).place(x=0,y=0)
        #===========
        img1_photo1=Image.open(r"images\photo1.jpg")
        img1_photo1=img1_photo1.resize((210,260),Image.ANTIALIAS)
        self.img1_photo1=ImageTk.PhotoImage(img1_photo1)
        img_photo_lbl1=Label(frame1,image=self.img1_photo1).place(x=420,y=20)
        
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
        img_mail_1=img_mail_1.resize((30,30),Image.ANTIALIAS)
        self.img_mail_1=ImageTk.PhotoImage(img_mail_1)
        
        name_lbl=Label(frame1,text="Name : Soumya Ranjan Seth",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=10)
        regd_lbl=Label(frame1,text="Regd. no : 1701335040",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=50)
        branch_lbl=Label(frame1,text="Branch : CSE",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=90)
        sem_lbl=Label(frame1,text="Sem : 8th",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=130)
        mail_lbl=Label(frame1,text=" : soumyaranjanseth60@gmail.com",image=self.img_mail_1,compound=LEFT,font=("times new roman",17,"bold"),fg="white",bg="black").place(x=15,y=170)

        face_lbl_1=Button(frame1,command=self.face_soumya,image=self.img1_1,compound=LEFT,cursor="hand2",font=("times new roman",20,"bold"),fg="white",bg="white").place(x=15,y=215)
        face_lbl1=Label(frame1,text=": https://www.facebook.com/soumyaranjanseth.gudu",font=("times new roman",13),fg="white",bg="black").place(x=60,y=220)
        
        insta_lbl_1=Button(frame1,command=self.insta_soumya,image=self.img1_2,compound=LEFT,cursor="hand2",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=255)
        insta_lbl1=Label(frame1,text=": https://instagram.com/mr._mind___blowing?igshid=1wv0wnywks8gi",font=("times new roman",9),fg="white",bg="black").place(x=58,y=262)

        #=======================frame1================================================================


        #=======================frame2================================================================
        frame2=Frame(self.root,bg="blue",bd=3,relief=RIDGE)
        frame2.place(x=640,y=50,width=640,height=300)
        #=======================Images==========================
        img2=Image.open(r"images\dev1.jpg")
        img2=img2.resize((640,300),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(img2)
        img_lbl2=Label(frame2,image=self.img2).place(x=0,y=0)
        #===========
        img1_photo2=Image.open(r"images\photo2.jpg")
        img1_photo2=img1_photo2.resize((200,260),Image.ANTIALIAS)
        self.img1_photo2=ImageTk.PhotoImage(img1_photo2)
        img_photo_lbl1=Label(frame2,image=self.img1_photo2).place(x=420,y=20)
        
        #====facebook============================
        img_sf_1=Image.open(r"images\facebook.png")
        img_sf_1=img_sf_1.resize((35,30),Image.ANTIALIAS)
        self.img_sf_1=ImageTk.PhotoImage(img_sf_1)
        #=======instagram========================
        img_si_1=Image.open(r"images\instagram.png")
        img_si_1=img_si_1.resize((35,30),Image.ANTIALIAS)
        self.img_si_1=ImageTk.PhotoImage(img_si_1)
        #=======mail========================
        img_mail_2=Image.open(r"images\mail1.webp")
        img_mail_2=img_mail_2.resize((30,30),Image.ANTIALIAS)
        self.img_mail_2=ImageTk.PhotoImage(img_mail_2)
        
        name_lbl=Label(frame2,text="Name : Shreeya Samarika Nayak",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=10)
        regd_lbl=Label(frame2,text="Regd. no : 1701335039",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=50)
        branch_lbl=Label(frame2,text="Branch : CSE",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=90)
        sem_lbl=Label(frame2,text="Sem : 8th",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=130)
        mail_lbl=Label(frame2,text=" : shreyasamarikanayak@gmail.com",image=self.img_mail_2,compound=LEFT,font=("times new roman",18,"bold"),fg="white",bg="black").place(x=10,y=170)

        face_lbl_2=Button(frame2,command=self.face_shreeya,image=self.img_sf_1,compound=LEFT,cursor="hand2",font=("times new roman",20,"bold"),fg="white",bg="white").place(x=10,y=215)
        face_lbl1=Label(frame2,text=": https://www.facebook.com/shreyaa.samarika",font=("times new roman",14),fg="white",bg="black").place(x=52,y=220)
        
        insta_lbl_2=Button(frame2,command=self.insta_shreeya,image=self.img_si_1,compound=LEFT,cursor="hand2",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=10,y=255)
        insta_lbl1=Label(frame2,text=": https://instagram.com/shreya_samarika?igshid=6ml4fpo6z6ex",font=("times new roman",11),fg="white",bg="black").place(x=50,y=260)

        # #=======================frame2================================================================


        #=======================frame3================================================================
        frame3=Frame(self.root,bg="green",bd=3,relief=RIDGE)
        frame3.place(x=0,y=350,width=640,height=300)
        #=======================Images==========================
        img3=Image.open(r"images\dev2.jpg")
        img3=img3.resize((640,300),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(img3)
        img_lbl3=Label(frame3,image=self.img3).place(x=0,y=0)
        #===========
        img1_photo3=Image.open(r"images\photo3.jpg")
        img1_photo3=img1_photo3.resize((210,260),Image.ANTIALIAS)
        self.img1_photo3=ImageTk.PhotoImage(img1_photo3)
        img_photo_lbl1=Label(frame3,image=self.img1_photo3).place(x=420,y=20)
        
        #====facebook============================
        img_af_1=Image.open(r"images\facebook.png")
        img_af_1=img_af_1.resize((35,30),Image.ANTIALIAS)
        self.img_af_1=ImageTk.PhotoImage(img_af_1)
        #=======instagram========================
        img_ai_1=Image.open(r"images\instagram.png")
        img_ai_1=img_ai_1.resize((35,30),Image.ANTIALIAS)
        self.img_ai_1=ImageTk.PhotoImage(img_ai_1)
        #=======mail========================
        img_mail_3=Image.open(r"images\mail1.webp")
        img_mail_3=img_mail_3.resize((30,30),Image.ANTIALIAS)
        self.img_mail_3=ImageTk.PhotoImage(img_mail_3)
        
        name_lbl=Label(frame3,text="Name : Ananya Kar",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=10)
        regd_lbl=Label(frame3,text="Regd. no : 1701335031",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=50)
        branch_lbl=Label(frame3,text="Branch : CSE",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=90)
        sem_lbl=Label(frame3,text="Sem : 8th",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=130)
        mail_lbl=Label(frame3,text=" : ananyakar6580@gmail.com",image=self.img_mail_3,compound=LEFT,font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=170)

        face_lbl_3=Button(frame3,command=self.face_kar,image=self.img_af_1,compound=LEFT,cursor="hand2",font=("times new roman",20,"bold"),fg="white",bg="white").place(x=15,y=215)
        face_lbl1=Label(frame3,text=":  https://www.facebook.com/manisha.dev.96592",font=("times new roman",13),fg="white",bg="black").place(x=55,y=220)
        
        insta_lbl_3=Button(frame3,command=self.insta_kar,image=self.img_ai_1,compound=LEFT,cursor="hand2",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=255)
        insta_lbl1=Label(frame3,text=": https://instagram.com/ananyakar95?igshid=zq2zwft96qd9",font=("times new roman",12),fg="white",bg="black").place(x=58,y=260)

        #=======================frame3================================================================


        #=======================frame4================================================================
        frame4=Frame(self.root,bg="yellow",bd=3,relief=RIDGE)
        frame4.place(x=640,y=350,width=640,height=300)
        #=======================Images==========================
        img4=Image.open(r"images\dev3.jpg")
        img4=img4.resize((640,300),Image.ANTIALIAS)
        self.img4=ImageTk.PhotoImage(img4)
        img_lbl4=Label(frame4,image=self.img4).place(x=0,y=0)
        #===========
        img1_photo4=Image.open(r"images\photo4.jpg")
        img1_photo4=img1_photo4.resize((200,260),Image.ANTIALIAS)
        self.img1_photo4=ImageTk.PhotoImage(img1_photo4)
        img_photo_lbl1=Label(frame4,image=self.img1_photo4).place(x=420,y=20)
        
        #====facebook============================
        img_1=Image.open(r"images\facebook.png")
        img_1=img_1.resize((35,30),Image.ANTIALIAS)
        self.img_1=ImageTk.PhotoImage(img_1)
        #=======instagram========================
        img_2=Image.open(r"images\instagram.png")
        img_2=img_2.resize((35,30),Image.ANTIALIAS)
        self.img_2=ImageTk.PhotoImage(img_2)
        #=======mail========================
        img_mail_4=Image.open(r"images\mail1.webp")
        img_mail_4=img_mail_4.resize((30,30),Image.ANTIALIAS)
        self.img_mail_4=ImageTk.PhotoImage(img_mail_4)
        
        name_lbl=Label(frame4,text="Name : Ashutosh Routray",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=10)
        regd_lbl=Label(frame4,text="Regd. no : 1701335032",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=50)
        branch_lbl=Label(frame4,text="Branch : CSE",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=90)
        sem_lbl=Label(frame4,text="Sem : 8th",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=15,y=130)
        mail_lbl=Label(frame4,text=" : routrayashutosh8@gmail.com",image=self.img_mail_4,compound=LEFT,font=("times new roman",19,"bold"),fg="white",bg="black").place(x=15,y=173)

        face_lbl_4=Button(frame4,command=self.face_ashu,image=self.img_1,compound=LEFT,cursor="hand2",font=("times new roman",13),fg="white",bg="white").place(x=15,y=215)
        face_lbl1=Label(frame4,text=": https://www.facebook.com/ashutosh.routray.14",font=("times new roman",13),fg="white",bg="black").place(x=60,y=220)
        
        insta_lbl_4=Button(frame4,command=self.insta_ashu,image=self.img_2,compound=LEFT,cursor="hand2",font=("times new roman",20,"bold"),fg="white",bg="black").place(x=12,y=255)
        insta_lbl1=Label(frame4,text=": https://instagram.com/a_happysoul_16?igshid=1r9ermuk92fei",font=("times new roman",11),fg="white",bg="black").place(x=51,y=260)

        #=======================frame4================================================================

    def face_soumya(self):
        webbrowser.open("https://www.facebook.com/soumyaranjanseth.gudu")
    def face_ashu(self):
        webbrowser.open("https://www.facebook.com/ashutosh.routray.14")
    def face_kar(self):
        webbrowser.open("https://www.facebook.com/manisha.dev.96592")
    def face_shreeya(self):
        webbrowser.open("https://www.facebook.com/shreyaa.samarika")

    def insta_shreeya(self):
        webbrowser.open("https://instagram.com/shreya_samarika?igshid=6ml4fpo6z6ex")
    def insta_ashu(self):
        webbrowser.open("https://instagram.com/a_happysoul_16?igshid=1r9ermuk92fei")
    def insta_kar(self):
        webbrowser.open("https://instagram.com/ananyakar95?igshid=zq2zwft96qd9")
    def insta_soumya(self):
        webbrowser.open("https://instagram.com/mr._mind___blowing?igshid=1wv0wnywks8gi")



if __name__ == '__main__':
    root=Tk()
    object=developer(root)
    root.mainloop()