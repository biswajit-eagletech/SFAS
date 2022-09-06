from tkinter import *
from tkinter import ttk,messagebox
from tkcalendar import *
from tkinter import filedialog
from PIL import ImageTk,Image
import pymysql
import cv2
import os
import numpy as np
from datetime import datetime
from time import strftime

class face_recgnition:
    def __init__(self,root):
        self.root=root
        self.root.title("Face Recgnition")
        self.root.geometry("1280x650+0+0")
        self.root.focus_force()
        self.root.grab_set()
        self.root.config(bg="snow")
        self.root.iconbitmap("images/rec1.ico")
        self.root.resizable(0,0)

        img1=Image.open(r"images\pic1.jpg")
        img1=img1.resize((1280,615),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img1)
        img_lbl1=Label(self.root,image=self.img1).place(x=0,y=50)

        title=Label(self.root,text="Face recognition",font=("Andalus",30,"bold"),bg="#262626",fg="cyan").place(x=9,y=0,relwidth=1)

        btn1=Button(self.root,command=self.face_recog,text="Face Recognition",font=("times new roman",20,"bold"),bd=2,relief=RAISED,bg="black",fg="light yellow",activebackground="light yellow",activeforeground="black",cursor="hand2").place(x=515,y=460,width=220,height=35)

    #=============================================================================================================================================================================================
    
    #===============================================
    def attendance(self,regd,name,gen,branch):
        with open("attendance.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((regd not in name_list) and (name not in name_list) and (gen not in name_list) and (branch not in name_list)):
                now=datetime.now()
                date_=now.strftime("%d/%m/%Y")
                time_=now.strftime("%H:%M:%S")
                f.writelines(f"\n{regd},{name},{branch},{time_},{date_},Present")
            
            
    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbour)

            coordinate=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()

                cur.execute("select `Regd. No.` from add_student where `Adm ID`="+str(id))
                regd=cur.fetchone()
                regd="+".join(regd)
                
                cur.execute("select `Name` from add_student where `Adm ID`="+str(id))
                name=cur.fetchone()
                name="+".join(name)
                
                cur.execute("select `Gender` from add_student where `Adm ID`="+str(id))
                gen=cur.fetchone()
                gen="+".join(gen)
                
                cur.execute("select `Branch` from add_student where `Adm ID`="+str(id))
                branch=cur.fetchone()
                branch="+".join(branch)
                

                if confidence>77:
                    cv2.putText(img,f"Regd. No: {regd}",(x,y-90),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name: {name}",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.8,(25,255,255),2)
                    cv2.putText(img,f"Gender: {gen}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(70,165,45),2)
                    cv2.putText(img,f"Branch: {branch}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(202,55,165),2)
                    self.attendance(regd,name,gen,branch)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"UNKNOWN FACE",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)

                coordinate=[x,y,w,h]

            return coordinate

        def recognize(img,clf,faceCascade):
            coordinate=draw_boundry(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Your attendance has been recorded Successfully",parent=self.root)





if __name__ == '__main__':
    root=Tk()
    obj=face_recgnition(root)
    root.mainloop()