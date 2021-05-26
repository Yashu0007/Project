from tkinter import *
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


window = tk.Tk()
window.title("Face_Recogniser")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
window.configure(background='plum3')
window.grid_rowconfigure(0, weight=2)
window.grid_columnconfigure(0, weight=2)

     
#bg=ImageTk.PhotoImage(file="a.jpg")
#bg_image=Label(image=bg).place(x=3,y=3,relwidth=3,relheight=1)

message = tk.Label(window,text="New Employee Registration",bg="mistyrose",fg="pale violet red",width=50,height=3,font=('Californian FB', 30, 'italic bold underline')) 
message.place(x=200, y=20)
lbl = tk.Label(window, text="Enter Employee ID:",width=20  ,height=2 ,bg="linen" ,fg="pale violet red"  ,font=('Lucida Calligraphy', 15, ' bold ') ) 
lbl.place(x=350, y=200)
txt = tk.Entry(window,width=16,fg="pale violet red",font=('times', 18, ' bold '))
txt.place(x=700, y=215)
lbl2 = tk.Label(window, text="Enter Name:",width=20  ,fg="pale violet red" ,bg="linen",height=2 ,font=('Lucida Calligraphy', 15, ' bold ')) 
lbl2.place(x=350, y=300)
txt2 = tk.Entry(window,width=16,fg="pale violet red",font=('times',18,'bold')  )
txt2.place(x=700, y=315)
lbl3 = tk.Label(window, text="STATUS:",width=20,fg="pale violet red",bg="linen",height=2 ,font=('Monotype Corsiva', 15,'bold underline ')) 
lbl3.place(x=400, y=400)
message = tk.Label(window, text="",fg="pale violet red",width=30,height=2,activebackground = "yellow" ,font=('times', 15,' bold ')) 
message.place(x=700, y=400)

def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faces=[]
    Ids=[]
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

def TakeImages():        
    Id=(txt.get())
    name=(txt2.get())
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)         
                sampleNum=sampleNum+1
                cv2.imwrite("TrainingImage\ " +name + "."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                cv2.imshow('frame',img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows() 
        #res = "Images Saved for ID : " + Id +" Name : "+ name
        row = [Id , name]
        with open('EmployeeDetails\EmployeeDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        #message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))    
    recognizer.save("TrainingImageLabel\Trainner.yml")   
    res = "New Employee Saved"#+",".join(str(f) for f in Id)

    message.configure(text= res)

  
clearButton = tk.Button(window, text="Clear", command=clear  ,fg="pale violet red"  ,width=18  ,height=1 ,activebackground = "palevioletred" ,font=('Lucida Calligraphy', 15, ' bold '))
clearButton.place(x=950, y=200)
clearButton2 = tk.Button(window, text="Clear", command=clear2  ,fg="pale violet red"   ,width=18  ,height=1, activebackground = "palevioletred" ,font=('Lucida Calligraphy', 15, ' bold '))
clearButton2.place(x=950, y=300)    
takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="pale violet red"   ,width=15  ,height=2, activebackground = "palevioletred" ,font=('Monotype Corsiva', 20, ' bold '))
takeImg.place(x=500, y=500)
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="pale violet red"   ,width=15  ,height=2, activebackground = "palevioletred" ,font=('Monotype Corsiva', 20, ' bold '))
quitWindow.place(x=800, y=500)
copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,font=('Brush Script MT', 25, 'italic bold underline'))
copyWrite.tag_configure("superscript", offset=10)

 
window.mainloop()
