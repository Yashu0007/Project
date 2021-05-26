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
    
def TrackImages():
    pqrs=0
    recognizer = cv2.face.LBPHFaceRecognizer_create()     
    recognizer.read("TrainingImageLabel\\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("EmployeeDetails\EmployeeDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Start Time','End Time','Duration']
    attendance = pd.DataFrame(columns = col_names)
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    xyz=[]
        
    abcd=0
    while(abcd<=60):
        while (pqrs<=20):
            ret, im =cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.2,5)
    
            for(x,y,w,h) in faces:
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
                if(conf < 50):
                    ts = time.time()      
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                
                    dt=datetime.datetime.now()
                    d=dt.strftime("%X")
        
                    aa=df.loc[df['Id'] == Id]['Name'].values
                    tt=str(Id)+"-"+aa
                    #attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                    xyz.append(d)
                else:
                    Id='Unknown'                
                    tt=str(Id)  
                if(conf > 75):
                    noOfFile=len(os.listdir("ImagesUnknown"))+1
                    cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
                cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)
            attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
            cv2.imshow('im',im) 
            if (cv2.waitKey(10)==ord('q')):
                #quit()
                break
            else:
                if(pqrs==20):
                    break
                time.sleep(2)
                pqrs+=2
        #print("pqrs=",pqrs)
        
        xyz=list(set(xyz))
        xyz.sort()
        print(xyz)
        if(len(xyz)>0):
            ts = time.time()      
            date = datetime.datetime.fromtimestamp(ts).strftime("%Y/%m/%d")
            startTime=xyz[0]
            endTime=xyz[-1]
            #if((len(xyz)*2)<=20):
            dur=(len(xyz)*2)-2
            #else:
                #dur=20
            aa=df.loc[df['Id'] == Id]['Name'].values
            aa=str(aa)
            aa=aa[2:-2]
            tt=str(Id)+"-"+aa
            attendance.loc[len(attendance)] = [Id,aa,date,startTime,endTime,dur]
            totaltime=20
            breaktime=totaltime-dur
            row = [Id , aa , date , startTime , endTime,totaltime,dur,breaktime]
            with open("Attendance\Attendance_"+str(aa)+".csv",'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
        #res=attendance
                csvFile.close()
            xyz=[]
        
            abcd+=pqrs
            pqrs=0
        else:
            print("Start Time ERROR!!!!")
            break
        #print(abcd)
        
        #cv2.destroyAllWindows()
        if (abcd==60):            
            break
        
            
TrackImages()

cv2.destroyAllWindows()
