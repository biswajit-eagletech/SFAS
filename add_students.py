from tkinter import *
from tkinter import ttk,messagebox
from tkcalendar import *
from tkinter import filedialog
from PIL import ImageTk,Image
import pymysql
import cv2
import os
import datetime
import time


class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Add Student")
        self.root.geometry("1055x525+215+120")
        self.root.resizable(0,0)
        self.root.focus_force()
        self.root.grab_set()
        self.root.config(bg="snow")
        self.root.iconbitmap("images/icon1.ico")
        self.root.resizable(0,0)

        #==========All Variables=======================
        self.doa_var=StringVar()
        self.doa_var.set(time.strftime("%d/%m/%Y"))
        self.admid_var=StringVar()
        self.regd_no_var=StringVar()
        self.name_var=StringVar()
        self.fname_var=StringVar()
        self.mname_var=StringVar()
        self.foccu_var=StringVar()
        self.email_var=StringVar()
        self.dob_var=StringVar()
        self.gender_var=StringVar()
        self.course_var=StringVar()
        self.branch_var=StringVar()
        self.con1_var=StringVar()
        self.con2_var=StringVar()
        self.blood_var=StringVar()
        self.religion_var=StringVar()
        self.search_var=StringVar()
        
        messagebox.showinfo("Info","Date format should be dd/mm/yyyy")
        #=============row0===================
        doa_lbl=Label(self.root,text="Date Of Admission",font=("times new roman",15),bg="snow",fg="#262626").place(x=20,y=0)
        doa_txt=Entry(self.root,textvariable=self.doa_var,font=("times new roman",15),bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=190,y=0,width=180,height=28)

        adm_id_lbl=Label(self.root,text="Admission Id",font=("times new roman",15),bg="snow",fg="#262626").place(x=440,y=0)
        self.adm_id_txt=Entry(self.root,textvariable=self.admid_var,font=("times new roman",15),bd=2,relief=SUNKEN,bg="light gray",fg="#262626")
        self.adm_id_txt.place(x=620,y=0,width=180,height=28)

        #=============row1===================
        regd_no_lbl=Label(self.root,text="Registration no.",font=("times new roman",15),bg="snow",fg="#262626").place(x=20,y=44)
        regd_no_txt=Entry(self.root,textvariable=self.regd_no_var,font=("times new roman",15),bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=190,y=44,width=180,height=28)

        name_lbl=Label(self.root,text="Student's Name",font=("times new roman",15),bg="snow",fg="#262626").place(x=440,y=44)
        name_txt=Entry(self.root,textvariable=self.name_var,font=("times new roman",15),bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=620,y=44,width=180,height=28)

        #=============row2===================
        father_name_lbl=Label(self.root,text="Father's Name",font=("times new roman",15),bg="snow",fg="#262626").place(x=20,y=90)
        father_name_txt=Entry(self.root,textvariable=self.fname_var,font=("times new roman",15),bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=190,y=90,width=180,height=28)

        mother_name_lbl=Label(self.root,text="Mother's Name",font=("times new roman",15),bg="snow",fg="#262626").place(x=440,y=90)
        mother_name_txt=Entry(self.root,textvariable=self.mname_var,font=("times new roman",15),bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=620,y=90,width=180,height=28)

        #=============row3===================
        father_occu_lbl=Label(self.root,text="Father's Occupation",font=("times new roman",15),bg="snow",fg="#262626").place(x=20,y=138)
        father_occu_cmb=ttk.Combobox(self.root,textvariable=self.foccu_var,font=("times new roman",15),state="readonly",justify="center")
        father_occu_cmb['values']=("Choose Occupation","Govt. Service","Pri. Service","Bussiness Man","Engineer","Doctor","Other")
        father_occu_cmb.current(0)
        father_occu_cmb.place(x=190,y=138,width=180,height=28)

        email_lbl=Label(self.root,text="E_mail Id",font=("times new roman",15),bg="snow",fg="#262626").place(x=440,y=138)
        email_txt=Entry(self.root,textvariable=self.email_var,font=("times new roman",15),bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=620,y=138,width=180,height=28)

        #=============row4===================
        dob_lbl=Label(self.root,text="Date of Birth",font=("times new roman",15),bg="snow",fg="#262626").place(x=20,y=188)
        dob_txt=Entry(self.root,textvariable=self.dob_var,font=("times new roman",15),bd=2,relief=SUNKEN,bg="light gray",fg="#262626")
        # dob_txt = DateEntry(self.root,textvariable=self.dob_var,font=("times new roman",15),state="readonly",date_pattern="dd/mm/yyyy",selectmode="day",year=2021,month=3,day=21)
        dob_txt.place(x=190,y=188,width=180,height=28)
        
        gender_lbl=Label(self.root,text="Gender",font=("times new roman",15),bg="snow",fg="#262626").place(x=440,y=188)
        gender_cmb=ttk.Combobox(self.root,textvariable=self.gender_var,font=("times new roman",15),state="readonly",justify="center")
        gender_cmb['values']=("Choose Gender","Male","Female","Other")
        gender_cmb.current(0)
        gender_cmb.place(x=620,y=188,width=180,height=28)

        #=============row5===================
        con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
        cur=con.cursor()
        cur.execute("SELECT `course_name` FROM `miscelleneous_course`")
        row=cur.fetchall()
        
        course_lbl=Label(self.root,text="Course",font=("times new roman",15),bg="snow",fg="#262626").place(x=20,y=238)
        course_cmb=ttk.Combobox(self.root,textvariable=self.course_var,font=("times new roman",15),state="readonly",justify="center")
        course_cmb['values']=row
        course_cmb.set("Choose Course")
        course_cmb.place(x=190,y=238,width=180,height=28)

        con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
        cur=con.cursor()
        cur.execute("SELECT `branch_name` FROM `miscelleneous_branch`")
        row=cur.fetchall()
        
        branch_lbl=Label(self.root,text="Branch",font=("times new roman",15),bg="snow",fg="#262626").place(x=440,y=238)
        branch_cmb=ttk.Combobox(self.root,textvariable=self.branch_var,font=("times new roman",15),state="readonly",justify="center")
        branch_cmb['values']=row
        branch_cmb.set("Choose Branch")
        branch_cmb.place(x=620,y=238,width=180,height=28)

        #=============row6===================
        pn1_lbl=Label(self.root,text="Contact No.",font=("times new roman",15),bg="snow",fg="#262626").place(x=20,y=285)
        pn1_txt=Entry(self.root,textvariable=self.con1_var,font=("times new roman",15),bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=190,y=285,width=180,height=28)
        
        pn2_lbl=Label(self.root,text="Alternate No.",font=("times new roman",15),bg="snow",fg="#262626").place(x=440,y=285)
        pn2_txt=Entry(self.root,textvariable=self.con2_var,font=("times new roman",15),bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=620,y=285,width=180,height=28)

        #=============row7===================
        blood_lbl=Label(self.root,text="Blood Group",font=("times new roman",15),bg="snow",fg="#262626").place(x=20,y=330)
        blood_cmb=ttk.Combobox(self.root,textvariable=self.blood_var,font=("times new roman",15),state="readonly",justify="center")
        blood_cmb['values']=("Choose Group","A+","A-","B+","B-","AB+","AB-","O+","O-")
        blood_cmb.current(0)
        blood_cmb.place(x=190,y=330,width=180,height=28)
        
        religion_lbl=Label(self.root,text="Religion",font=("times new roman",15),bg="snow",fg="#262626").place(x=440,y=330)
        religion_cmb=ttk.Combobox(self.root,textvariable=self.religion_var,font=("times new roman",15),state="readonly",justify="center")
        religion_cmb['values']=("Choose Religion","Hindu","Muslim","Christian","Jain","Budh","Other")
        religion_cmb.current(0)
        religion_cmb.place(x=620,y=330,width=180,height=28)

        #=============row6===================
        addr_lbl=Label(self.root,text="Address",font=("times new roman",15),bg="snow",fg="#262626").place(x=20,y=375)
        self.addr_txt=Text(self.root,bd=2,relief=SUNKEN,bg="light gray",fg="#262626")
        self.addr_txt.place(x=190,y=375,width=300,height=80)
        
        #=====Search Students==========================
        search_lbl=Label(self.root,text="Search Student :",font=("times new roman",16,"bold"),bg="snow",fg="red").place(x=500,y=380)
        adm_lbl=Label(self.root,text="Admm. Id",font=("times new roman",16,"bold"),bg="snow",fg="green").place(x=660,y=380)
        adm_txt=Entry(self.root,textvariable=self.search_var,font=("times new roman",15),bd=2,relief=SUNKEN,bg="light gray",fg="#262626").place(x=770,y=380,width=180,height=28)
        self.search_btn=Button(self.root,command=self.search,text="🔍",font=("times new roman",16,"bold"),bd=2,relief=RAISED,bg="black",fg="white",activebackground="cyan",activeforeground="black",cursor="hand2")
        self.search_btn.place(x=965,y=377,width=80,height=30)

        #===============Radio Buttons====================
        self.var_option_type=StringVar()
        self.var_option_type.set("Select")
        radio_btn1=Radiobutton(self.root,variable=self.var_option_type,value="Select",text="Select",font=("times new roman",13,"bold"),bg="snow",fg="black",activeforeground="black",activebackground="snow",cursor="hand2").place(x=20,y=470)
        radio_btn2=Radiobutton(self.root,variable=self.var_option_type,value="Yes",text="Select Photo Sample",font=("times new roman",13,"bold"),bg="snow",fg="black",activeforeground="black",activebackground="snow",cursor="hand2").place(x=120,y=470)
        radio_btn3=Radiobutton(self.root,variable=self.var_option_type,value="No",text="No Photo Sample",font=("times new roman",13,"bold"),bg="snow",fg="black",activeforeground="black",activebackground="snow",cursor="hand2").place(x=330,y=470)

        #=============All Buttons=======================
        self.save_btn=Button(self.root,command=self.add_student,text="Save",font=("times new roman",15,"bold"),bd=2,relief=RAISED,bg="black",fg="white",activebackground="light green",activeforeground="black",cursor="hand2")
        self.save_btn.place(x=510,y=430,width=130,height=35)
        
        self.update_btn=Button(self.root,command=self.update_student,state=DISABLED,text="Update",font=("times new roman",15,"bold"),bd=2,relief=RAISED,bg="black",fg="white",activebackground="orange",activeforeground="black",cursor="hand2")
        self.update_btn.place(x=645,y=430,width=130,height=35)
        
        self.delete_btn=Button(self.root,command=self.delete_data,state=DISABLED,text="Delete",font=("times new roman",15,"bold"),bd=2,relief=RAISED,bg="black",fg="white",activebackground="red",activeforeground="black",cursor="hand2")
        self.delete_btn.place(x=780,y=430,width=130,height=35)
        
        self.reset_btn=Button(self.root,command=self.clear_data,text="Reset",font=("times new roman",15,"bold"),bd=2,relief=RAISED,bg="black",fg="white",activebackground="purple",activeforeground="white",cursor="hand2")
        self.reset_btn.place(x=915,y=430,width=130,height=35)
        
        self.take_photo_btn=Button(self.root,command=self.generate_data,state=DISABLED,text="Take Photo Sample",font=("times new roman",15,"bold"),bd=2,relief=RAISED,bg="black",fg="white",activebackground="light blue",activeforeground="black",cursor="hand2")
        self.take_photo_btn.place(x=510,y=470,width=265,height=35)
        
        self.update_photo_btn=Button(self.root,command=self.generate_data,state=DISABLED,text="Update Photo Sample",font=("times new roman",15,"bold"),bd=2,relief=RAISED,bg="black",fg="white",activebackground="light pink",activeforeground="black",cursor="hand2")
        self.update_photo_btn.place(x=780,y=470,width=265,height=35)
        
        # upload_btn=Button(self.root,command=self.open_file,text="Upload",font=("times new roman",15,"bold"),bd=2,relief=RAISED,bg="black",fg="white",activebackground="plum",activeforeground="black",cursor="hand2").place(x=870,y=315,width=130,height=30)

        #==========Label for photo=========================
        # self.photo_lbl=Label(self.root,text="Add\nStudents\nPhoto",font=("times new roman",18,"bold"),cursor="hand2",bd=5,relief=RIDGE,bg="light gray",fg="peru")
        # self.photo_lbl.place(x=830,y=80,width=200,height=200)

    def open_file(self):
        file_img=filedialog.askopenfilename(initialdir="/images",title="Select Student Images",filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*")),parent=self.root)
        self.open_img=Image.open(file_img)
        self.open_img.thumbnail((250,250))
        self.open_img=ImageTk.PhotoImage(self.open_img)
        self.photo_lbl.config(image=self.open_img)

    def add_student(self):
        if self.regd_no_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All Fields are required ?",parent=self.root)
        elif self.var_option_type.get()=="Select":
            messagebox.showerror("Error","Please Select the Type ?")
        elif self.var_option_type.get()=="Yes":
            messagebox.showwarning("Sorry","You can not Take Sample Here.\nPlease First add the Data!!!!",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("select * from add_student where `Adm ID`=%s",(self.admid_var.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Admission Id is Available\nTry with another",parent=self.root)
                else:
                    cur.execute("INSERT INTO `add_student` VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.admid_var.get(),
                        self.doa_var.get(),
                        self.regd_no_var.get(),
                        self.name_var.get(),
                        self.fname_var.get(),
                        self.mname_var.get(),
                        self.foccu_var.get(),
                        self.email_var.get(),
                        self.dob_var.get(),
                        self.gender_var.get(),
                        self.course_var.get(),
                        self.branch_var.get(),
                        self.con1_var.get(),
                        self.con2_var.get(),
                        self.blood_var.get(),
                        self.religion_var.get(),
                        self.addr_txt.get('1.0',END),
                        self.var_option_type.get()
                        )
                        )
                    con.commit()
                    self.clear_data()
                    messagebox.showinfo("Successs","Student Added Successfully !!",parent=self.root)                
                con.close()

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def search(self):
        if self.search_var.get()=="":
            messagebox.showerror("Error","Addmission ID must be required !!!",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("select * from add_student where `Adm ID`=%s",(self.search_var.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Addmission ID !!\nPlz try with another Addmission ID",parent=self.root)
                else:
                    self.doa_var.set(row[1])
                    self.admid_var.set(row[0])
                    self.regd_no_var.set(row[2])
                    self.name_var.set(row[3])
                    self.fname_var.set(row[4])
                    self.mname_var.set(row[5])
                    self.foccu_var.set(row[6])
                    self.email_var.set(row[7])
                    self.dob_var.set(row[8])
                    self.gender_var.set(row[9])
                    self.course_var.set(row[10])
                    self.branch_var.set(row[11])
                    self.con1_var.set(row[12])
                    self.con2_var.set(row[13])
                    self.blood_var.set(row[14])
                    self.religion_var.set(row[15])
                    self.addr_txt.delete('1.0',END)
                    self.addr_txt.insert(END,row[16])
                    self.var_option_type.set(row[17])
                    self.update_btn.config(state=NORMAL)
                    self.delete_btn.config(state=NORMAL)
                    self.save_btn.config(state=DISABLED)
                    self.update_photo_btn.config(state=NORMAL)
                    self.take_photo_btn.config(state=NORMAL)
                    self.search_btn.config(state=DISABLED)
                    self.adm_id_txt.config(state="readonly")

            except Exception as ex:
                    messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    

    def update_student(self):
        if self.regd_no_var.get()=="":
            messagebox.showerror("Error","Registation No. must Required ?",parent=self.root)
        else:
            ask=messagebox.askyesno("Update","Do you want to Update ?",parent=self.root)
            if ask > 0:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("UPDATE `add_student` SET `Regd. No.`=%s,`Name`=%s,`Father's Name`=%s,`Mother's Name`=%s,`Occupation`=%s,`E_mail id`=%s,`D.O.B`=%s,`Gender`=%s,`Course`=%s,`Branch`=%s,`Contact1`=%s,`Contact2`=%s,`Blood Group`=%s,`Religion`=%s,`Address`=%s,`Face_Photo`=%s WHERE `Adm ID`=%s",(
                            self.regd_no_var.get(),
                            self.name_var.get(),
                            self.fname_var.get(),
                            self.mname_var.get(),
                            self.foccu_var.get(),
                            self.email_var.get(),
                            self.dob_var.get(),
                            self.gender_var.get(),
                            self.course_var.get(),
                            self.branch_var.get(),
                            self.con1_var.get(),
                            self.con2_var.get(),
                            self.blood_var.get(),
                            self.religion_var.get(),
                            self.addr_txt.get('1.0',END),
                            self.var_option_type.get(),
                            self.admid_var.get()
                            )
                            )
                con.commit()
                self.clear_data()
                messagebox.showinfo("Success","Data Updated Successfully !",parent=self.root)
                con.close()    
            else:
                return

    def delete_data(self):
        if self.regd_no_var.get()=="":
            messagebox.showerror("Error","Registration No. msut required ?",parent=self.root)
        else:
            ask=messagebox.askokcancel("Delete","Do you want to Delete Data",parent=self.root)
            if ask > 0:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("DELETE from add_student WHERE `Adm ID`=%s",self.admid_var.get())
                con.commit()
                self.clear_data()
                messagebox.showinfo("Success","Data Deleted Successfully 1",parent=self.root)
                con.close()  
            else:
                return


    def clear_data(self):
        self.admid_var.set("")
        self.doa_var.set(time.strftime("%d/%m/%Y"))
        self.regd_no_var.set("")
        self.name_var.set("")
        self.fname_var.set("")
        self.mname_var.set("")
        self.foccu_var.set("Choose Occupation")
        self.email_var.set("")
        self.dob_var.set("")
        self.gender_var.set("Choose Gender")
        self.course_var.set("Choose Course")
        self.branch_var.set("Choose Branch")
        self.con1_var.set("")
        self.con2_var.set("")
        self.blood_var.set("Choose Group")
        self.religion_var.set("Choose Religion")
        self.search_var.set("")
        self.addr_txt.delete('1.0',END)
        self.var_option_type.set("Select")
        self.update_btn.config(state=DISABLED)
        self.delete_btn.config(state=DISABLED)
        self.save_btn.config(state=NORMAL)
        self.update_photo_btn.config(state=DISABLED)
        self.take_photo_btn.config(state=DISABLED)
        self.search_btn.config(state=NORMAL)
        self.adm_id_txt.config(state=NORMAL)

#===========creating folder==========================
        if os.path.exists('cap_images')==False:
            os.mkdir('cap_images')

#========================Generating data sets from Students===============================================================================
    def generate_data(self):
        if self.regd_no_var.get()=="":
            messagebox.showerror("Error","Registation No. must Required ?",parent=self.root)
        elif self.var_option_type.get()=="Select":
            messagebox.showerror("Error","Plz Choose Option",parent=self.root)
        elif self.var_option_type.get()=="No":
            messagebox.showerror("Error"," You cann't Select No Option",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="student_face_system")
                cur=con.cursor()
                cur.execute("select * from add_student")
                myresult=cur.fetchall()
                id=0
                for x in myresult:
                    id+=1
                cur.execute("UPDATE `add_student` SET `Adm Date`=%s,`Regd. No.`=%s,`Name`=%s,`Father's Name`=%s,`Mother's Name`=%s,`Occupation`=%s,`E_mail id`=%s,`D.O.B`=%s,`Gender`=%s,`Course`=%s,`branch`=%s,`Contact1`=%s,`Contact2`=%s,`Blood Group`=%s,`Religion`=%s,`Address`=%s,`Face_Photo`=%s WHERE `Adm ID`=%s",(
                                self.dob_var.get(),
                                self.regd_no_var.get(),
                                self.name_var.get(),
                                self.fname_var.get(),
                                self.mname_var.get(),
                                self.foccu_var.get(),
                                self.email_var.get(),
                                self.dob_var.get(),
                                self.gender_var.get(),
                                self.course_var.get(),
                                self.branch_var.get(),
                                self.con1_var.get(),
                                self.con2_var.get(),
                                self.blood_var.get(),
                                self.religion_var.get(),
                                self.addr_txt.get('1.0',END),
                                self.var_option_type.get(),
                                self.admid_var.get()==id+1
                                )
                                )
                con.commit()
                con.close()  
            #=========Frontal Face================================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            
                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #min. neighbour=5

                    for (x,y,w,h) in faces:
                        face_crop=img[y:y+h , x:x+w]
                        return face_crop
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,frame_=cap.read()
                    if face_crop(frame_) is not None:
                        img_id+=1
                        face=cv2.resize(face_crop(frame_),(500,500))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="cap_images/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,"image_"+str(img_id),(80,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),1)
                        cv2.imshow("Crop Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success","Datasets Generated Suucessfully!!!!",parent=self.root)
                self.delete_btn.config(state=DISABLED)
                self.reset_btn.config(state=DISABLED)
                self.take_photo_btn.config(state=DISABLED)
                self.update_photo_btn.config(state=DISABLED)

            except Exception as ex:
                    messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    

if __name__=="__main__":
    root=Tk()
    object=student(root)
    root.mainloop()