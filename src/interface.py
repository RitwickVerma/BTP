import tkinter as tk
import serial
import time
import os
from queue import Queue
from PIL import ImageTk
from src.arduino import Arduino

class Interface:
    def __init__(self,root,ardlist):
        #self.ardlist=ardlist
        self.root=root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.car_running=False

        self.ar_0=ardlist[0]
        self.ar_1=ardlist[1]
        self.ar_2=ardlist[2]
        self.ar_3=ardlist[3]
        
    
    def guiloop(self):
     
        self.text_usfl=tk.StringVar(self.root)
        self.text_usfr=tk.StringVar(self.root)
        self.text_usbl=tk.StringVar(self.root)
        self.text_usbr=tk.StringVar(self.root)
        self.text_time=tk.StringVar(self.root)
        self.text_rpm=tk.StringVar(self.root)
        

        photo_vehicle=ImageTk.PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+"/img_res/car.png")
        center_img=tk.Label(self.root,image=photo_vehicle,relief='flat',bg='white')
        picture_height=photo_vehicle.height()
        picture_width=photo_vehicle.width()             
        center_img.place(x=(self.screen_width-picture_width)/2,y=(self.screen_height-picture_height)/2)    
       
        self.main_frame=tk.Frame(self.root,bg='')
        
        label_usfl=tk.Label(self.main_frame,textvariable=self.text_usfl,bg='white',font=("Courier", 24),fg='black',anchor="center")
        label_usfl.place(x=((self.screen_width-picture_width)/2),y=((self.screen_height-picture_height)/2)+250)


        label_usfr=tk.Label(self.main_frame,textvariable=self.text_usfr,bg='white',font=("Courier", 24),fg='black')
        label_usfr.place(x=((self.screen_width-picture_width)/2)+490,y=((self.screen_height-picture_height)/2)+250)

        label_usbl=tk.Label(self.main_frame,textvariable=self.text_usbl,bg='white',font=("Courier", 24),fg='black')
        label_usbl.place(x=((self.screen_width-picture_width)/2),y=((self.screen_height-picture_height)/2)+750)

        label_usbr=tk.Label(self.main_frame,textvariable=self.text_usbr,bg='white',font=("Courier", 24),fg='black')
        label_usbr.place(x=((self.screen_width-picture_width)/2)+490,y=((self.screen_height-picture_height)/2)+750)

        label_rpm=tk.Label(self.main_frame,textvariable=self.text_rpm,bg='white',font=("Courier", 32),fg='black')
        label_rpm.place(x=(self.screen_width/2)-150,y=100)
 
        label_Time=tk.Label(self.root,textvariable=self.text_time,bg='white',font=("Courier", 28),fg='black')
        label_Time.place(x=5,y=5)
                        
        self.button_relay=tk.Button(self.root,height=2,width=10,text="Start Car",command=self.toggle_car,bg='#009688',font=("Courier", 42),activeforeground='white',fg='white',bd=0,justify='center', highlightthickness=0)
        self.button_relay.place(x=self.screen_width-360,y=0)

        self.update_time()
        self.root.mainloop()


    def toggle_car(self):
        if self.car_running:
            self.ar_0.senddata('x')
            self.button_relay.config(text="Start Car",bg='#009688')
            self.car_running=False
            self.main_frame.pack_forget()

        else:
            """for q in self.mainbuf:
                with q.mutex:
                    q.queue.clear()"""
            self.ar_0.senddata('o')
            self.button_relay.config(text="Stop Car",bg='#ff6347')
            self.car_running=True
            self.main_frame.pack(fill='both',expand=True)
            self.updateall()

    def updateall(self):
        self.update_ar_1()
        self.update_ar_2()
        self.update_ar_3()
        if(self.car_running):
            self.root.after(10,self.updateall)

    def update_ar_1(self):
        sensdata=self.ar_1.getcurr_data()
        self.text_rpm.set(sensdata['psrpm']+" rpm")

    def update_ar_2(self):
        sensdata=self.ar_2.getcurr_data()

        self.text_usfl.set(sensdata['usfld'])
        self.text_usfr.set(sensdata['usfrd'])
        
    
    def update_ar_3(self):
        sensdata=self.ar_3.getcurr_data()

        self.text_usbl.set(sensdata['usbld'])
        self.text_usbr.set(sensdata['usbrd'])
    
    
    def update_time(self):
        self.text_time.set(time.strftime("%I:%M %p",time.localtime()))
        self.root.after(100,self.update_time)