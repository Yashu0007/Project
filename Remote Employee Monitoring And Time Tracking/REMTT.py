from tkinter import * 
from PIL import ImageTk
from tkinter import messagebox
import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
root=Tk()
class Login:
    def __init__(self,root):
        
        self.root=root
        self.root.title("Login")
        self.root.geometry("1399x750+10+10")   
        #self.bg=ImageTk.PhotoImage(file="image.jpg")
        #self.bg_image=Label(self.root,image=self.bg).place(x =0, y =0,relwidth=1,relheight=1)
        
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)
        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Manager Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
        
        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)
        
        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        login_btn=Button(self.root,command=self.login_function,text="Login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=200,y=460,width=180,height=39)
        register=Button(self.root,text="New Registration",command=self.registration,fg="white",bg="#d77337",font=("times new roman",20)).place(x=400,y=460,width=210,height=40)

        
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif (self.txt_user.get()!="Yash" or self.txt_pass.get()!="yash@123")  and (self.txt_user.get()!="Rohan" or self.txt_pass.get()!="rohan123"):
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            newlogin=Toplevel(root)
            newlogin.title("Department")
            newlogin.geometry("1399x750+10+10")
            #newlogin.bg=ImageTk.PhotoImage(file="a3.jpg")
            #newlogin.bg_image=Label(newlogin,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
            Label(newlogin,text="Select Department",font=("Goudy old style",35,"bold"),fg="#d25d17",bg="white").place(x=330,y=30)
            
            def product():
                def rohan():
                    os.chdir('C:\\Users\\User\\Jupitor Notebook\\Final Year Project\\Remote Employee Monitoring And Time Tracking\\Attendance')
                    os.system('start excel.exe Attendance_Rohan')
                def yash():
                    os.chdir('C:\\Users\\User\\Jupitor Notebook\\Final Year Project\\Remote Employee Monitoring And Time Tracking\\Attendance')
                    os.system('start excel.exe Attendance_Yash')
                def kazi():
                    os.chdir('C:\\Users\\User\\Jupitor Notebook\\Final Year Project\\Remote Employee Monitoring And Time Tracking\\Attendance')
                    os.system('start excel.exe Attendance_Kazi')
                def krishna():
                    os.chdir('C:\\Users\\User\\Jupitor Notebook\\Final Year Project\\Remote Employee Monitoring And Time Tracking\\Attendance')
                    os.system('start excel.exe Attendance_Krishna')
                newproduct=Toplevel(root)
                newproduct.title("Production Department")
                newproduct.geometry("1399x750+10+10")
                #newproduct.bg=ImageTk.PhotoImage(file="a3.jpg")
                Label(newproduct,text="Production Department",font=("Goudy old style",25,"bold"),fg="#d25d17",bg="white").place(x=330,y=30)
                emp1=Button(newproduct,text="Rohan",command=rohan,fg="blue",bg="white",font=("times new roman",20)).place(x=300,y=120,width=200,height=55)
                emp2=Button(newproduct,text="Yash",fg="blue",command=yash,bg="white",font=("times new roman",20)).place(x=300,y=175,width=200,height=55)
                emp3=Button(newproduct,text="Kazi",fg="blue",command=kazi,bg="white",font=("times new roman",20)).place(x=300,y=230,width=200,height=55)
                emp4=Button(newproduct,text="Krishna",fg="blue",command=krishna,bg="white",font=("times new roman",20)).place(x=300,y=285,width=200,height=55)
                quitWindow =Button(newproduct, text="Quit", command=newproduct.destroy  ,fg="light blue"  ,bg="white" ,font=('times new roman', 20, ' bold '))
                quitWindow.place(x=300, y=400,width=200  ,height=55)
                
    
            production=Button(newlogin,text="Production",command=product,fg="blue",bg="white",font=("times new roman",20)).place(x=300,y=200,width=200,height=55)
            tesing=Button(newlogin,text="Testing",fg="blue",bg="white",font=("times new roman",20)).place(x=550,y=200,width=200,height=55)
            design=Button(newlogin,text="Design",fg="blue",bg="white",font=("times new roman",20)).place(x=300,y=300,width=200,height=55)
            management=Button(newlogin,text="Management",fg="blue",bg="white",font=("times new roman",20)).place(x=550,y=300,width=200,height=55)
            quitWindow =Button(newlogin, text="Quit", command=newlogin.destroy  ,fg="light blue"  ,bg="white" ,font=('times new roman', 20, ' bold '))
            quitWindow.place(x=425, y=400,width=200  ,height=55)

            

            
    def registration(self):
        newWindow=Toplevel(root)
        newWindow.title("Registration")
        newWindow.resizable(False,False) 
        newWindow.geometry("800x750+10+10")
        Label(newWindow,text="New Manager Registration",font=("Goudy old style",25,"bold"),fg="#d25d17",bg="white").place(x=230,y=30)
        
        lbl_user=Label(newWindow,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(newWindow,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)
        
        lbl_pass=Label(newWindow,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(newWindow,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        def store():
            user=(self.txt_user.get())
            password=(self.txt_pass.get())
            row = [user , password]
            with open('Manager\list.csv','a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            res = "New Registration Saved...Click Quit"
            message.configure(text=res)
            
            
        save_btn=Button(newWindow,text="Save",command=store,fg="white",bg="#d77337",font=("times new roman",20)).place(x=90,y=300,width=180,height=39)
        quitWindow =Button(newWindow, text="Quit", command=newWindow.destroy  ,fg="white"  ,bg="#d77337" ,font=('times new roman', 20, ' bold '))
        quitWindow.place(x=300, y=300,width=180  ,height=39)

        lbl3 = Label(newWindow, text="STATUS : ",width=15  ,fg="white"  ,bg="rosybrown2"  ,height=2 ,font=('Monotype Corsiva', 15, ' bold underline ')) 
        lbl3.place(x=70, y=370)
        message = Label(newWindow, text="" ,bg="rosybrown2"  ,fg="white"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
        message.place(x=270, y=370)


        
        
    
        
        

obj=Login(root)
root.mainloop()