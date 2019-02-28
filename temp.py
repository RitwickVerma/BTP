import tkinter as tk
import serial
import time
import os
from PIL import ImageTk
#import RPi.GPIO as GPIO 
 
#Function Definitions
 
#Find Connected Arduinos
 
def find_dev():
    global left_ar,right_ar,rpm_ar,cabin_ar,back_ar
    devices=os.listdir("/dev")
    for dev in devices:
        if dev[0:6]=="ttyUSB" or dev[0:6]=="ttyACM":
            arduino=serial.Serial("/dev/" + str(dev),9600)
            assign=arduino.readline()
            assign=arduino.readline()
            
            para=str(assign).split() 
            #print(para)
            if(para[0][2:]=="b'Distancelf:"):
                left_ar=arduino
            elif para[0]=="b'Distancerf:":
                right_ar=arduino
            elif para[0]=="b'RPM:":
                rpm_ar=arduino
            elif para[0]=="b'cabin":
                cabin_ar=arduino
            elif para[0]=="b'Distancebl":
                back_ar=arduino
            
 
#Update Ultrasonic Sensor Labels-Left 
 
def update_left():
    global left_ar
    data=left_ar.readline()
    data_split=str(data).split()
    label_lf.config(text=data_split[1])
    label_lb.config(text=data_split[3])
    if int(data_split[1])<50:
        label_lf.place(x=((screen_width-picture_width)/2)+50,y=((screen_height-picture_height)/2)+250)
    else:
        label_lf.place(x=screen_width+1,y=screen_height+1)
    if int(data_split[3])<50:
        label_lb.place(x=((screen_width-picture_width)/2)+50,y=((screen_height+picture_height)/2)-250)
    else:
        label_lb.place(x=screen_width+1,y=screen_height+1)
 
#Update Ultrasonic Sensor Labels-Right
 
def update_right():
    global right_ar
    data=right_ar.readline()
    data_split=str(data).split()
    label_rf.config(text=data_split[1])
    label_rb.config(text=data_split[3])
    if int(data_split[1])<50:
        label_rf.place(x=((screen_width+picture_width)/2)+20,y=((screen_height-picture_height)/2)+30)
    else:
        label_rf.place(x=screen_width+1,y=screen_height+1)
    if int(data_split[3])<50:
        label_rb.place(x=((screen_width+picture_width)/2)+20,y=((screen_height+picture_height)/2)-30)
    else:
        label_rb.place(x=screen_width+1,y=screen_height+1)
 
#Update Ultrasonic Sensor Labels-Back
 
def update_back():
    global back_ar
    data=back_ar.readline()
    data_split=str(data).split()
    label_bl.config(text=data_split[1])
    label_br.config(text=data_split[3])
    if int(data_split[1])<50:
        label_bl.place(x=((screen_width-picture_width)/2)+20,y=((screen_height+picture_height)/2)+30)
    else:
        label_bl.place(x=screen_width+1,y=screen_height+1)
    if int(data_split[3])<50:
        label_br.place(x=((screen_width+picture_width)/2)-20,y=((screen_height+picture_height)/2)+30)
    else:
        label_br.place(x=screen_width+1,y=screen_height+1)
 
#Update Time
 
def update_time():
    global startTime
    label_Time.config(text="Time of Operation " + str(int((time.time()-startTime)/3600))+" Hours "+str(int((time.time()-startTime)/60))+" Minutes",fg="black",bg="yellow") 
    label_Time.place(x=0,y=0)
    
#Relay Control Button Toggle    
    
def relay_control():
    global flag
    if flag==0:
        #GPIO.output(40, GPIO.HIGH)
        relay_button.config(text="Turn Off",command=relay_control)
        flag=1
    elif flag==1:
        #GPIO.output(40, GPIO.LOW)
        relay_button.config(text="Turn On",command=relay_control)
        flag=0
 
#Update
        
def update():
    update_left()
    #update_right()
    #update_back()
    #update_rpm()
    update_time()
    #Recursion for each update
    root.after(1000, update)
 
 
 
#Initialize Time
 
startTime=time.time()
 
#Initialize RPi for GPIO
 
##GPIO.setmode(GPIO.BOARD)      
##GPIO.setup(40,GPIO.OUT,initial=GPIO.LOW)        
flag = 0 #for Relay Control
 
#Tkinter for GUI
 
root=tk.Tk()
 
#Fullscreen
 
root.attributes('-zoomed', True)
root.wm_attributes('-alpha', 0.7)  
root.configure(bg='white')
 
#Getting Screen Resolution
 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
 
#Center Image
photo_vehicle=ImageTk.PhotoImage(file="/home/ritwick/Documents/Arduino/US/car.png")
center_img=tk.Label(root,image=photo_vehicle,relief='flat',bg='white')

picture_height=photo_vehicle.height()
picture_width=photo_vehicle.width()
 
center_img.place(x=(screen_width-picture_width)/2,y=(screen_height-picture_height)/2)
 
#Labels for Ultrasonic Sensor
 
label_lf= tk.Label(root,text="lf")
label_lf.config(bg='white',font=("Courier", 32),fg='black')
label_lb= tk.Label(root,text="lb")
label_lb.config(bg='white',font=("Courier", 32),fg='black')
label_rf= tk.Label(root,text="rf")
label_rb= tk.Label(root,text="rb")
label_bl= tk.Label(root,text="bl")
label_br= tk.Label(root,text="br")
 
#Label for RPM Sensor
 
label_rpm=tk.Label(root,text="RPM",bg="yellow",fg="black")
label_rpm.place(x=(screen_width/2)-10,y=(screen_height/2)-10)
 
#Label for Time
 
label_Time=tk.Label(root,text=startTime)
 
#Button to Control Relay
 
relay_button=tk.Button(root,text="Turn On",command=relay_control)
relay_button.place(x=(screen_width/2)-10,y=((screen_height+picture_height)/2)+60)
 
#Find and Assign Connected Arduinos
 
find_dev()
 
#Update Each Component
 
update()
 
#Mainloop
 
root.mainloop()