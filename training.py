from tkinter import *
from tkinter import ttk,messagebox
from tkcalendar import *
from tkinter import filedialog
from PIL import ImageTk,Image
import pymysql
import cv2
import os
import numpy as np

class train_data:
    def __init__(self,root):
        self.root=root
        self.root.title("Add Student")
        self.root.geometry("1280x650+0+0")
        self.root.focus_force()
        self.root.grab_set()
        self.root.config(bg="snow")
        self.root.iconbitmap("images/icon2.ico")
        self.root.resizable(0,0)

        img1=Image.open(r"images\train1.jpg")
        img1=img1.resize((1280,650),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img1)
        
        self.lbl1=Label(self.root,image=self.img1).place(x=0,y=0,relwidth=1)

        title=Label(self.root,text="TRAIN THE SYSTEM",font=("goudy old style",35,"bold"),bg="light blue",fg="purple").place(x=0,y=1,relwidth=1)

        self.var_chk=IntVar()
        btn_ckeck=Checkbutton(self.root,text="Do You Want To See The Data While Training The System",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",15,"bold"),bd=0,bg="#c1e0e6",fg="black",activebackground="#c1e0e6",activeforeground="black",cursor="hand2").place(x=130,y=370)

        btn_start=Button(self.root,command=self.train_sample,text="Start Training",font=("times new roman",20,"bold"),bd=2,relief=RAISED,bg="yellow",fg="black",activebackground="black",activeforeground="yellow",cursor="hand2").place(x=260,y=435,width=240,height=40)

        
    def train_sample(self):
        data_dir=("cap_images")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L")  #convert to gray scale image
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            if self.var_chk.get()==1:
                cv2.imshow("Training Data",imagenp)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)
        
        #======================================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed !!!!!",parent=self.root)
        self.var_chk.set(0)
    


if __name__ == '__main__':
    root=Tk()
    obj=train_data(root)
    root.mainloop()