import tkinter as tk
import serial
import time
import os
from gpiozero import LED
from queue import Queue
from PIL import ImageTk, Image
from src.arduino import Arduino

class Interface:
    def __init__(self,root,ardlist):
        self.root=root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        normal_width = 1920
        normal_height = 1080
        self.rw = self.screen_width / normal_width
        self.rh = self.screen_height / normal_height
        self.sf = ((self.rw + self.rh) / 2)
        self.car_running=False

        self.relay_pin=LED(3)
        self.ar_0=ardlist[0]
        self.ar_1=ardlist[1]
        self.ar_2=ardlist[2]
        
    
    def guiloop(self):
     
        self.text_usfl=tk.StringVar(self.root)
        self.text_usfr=tk.StringVar(self.root)
        self.text_usbl=tk.StringVar(self.root)
        self.text_usbr=tk.StringVar(self.root)
        self.text_time=tk.StringVar(self.root)
        self.text_rpm=tk.StringVar(self.root)
        
        photo_vehicle=Image.open(os.path.dirname(os.path.realpath(__file__))+"/img_res/car.png")
        photo_vehicle=photo_vehicle.resize((int(self.screen_width*0.25),int(self.screen_height*0.75)),Image.ANTIALIAS)
        photo_vehicle=ImageTk.PhotoImage(photo_vehicle)
        center_img=tk.Label(self.root,image=photo_vehicle,relief='flat',bg='white')
        picture_height=photo_vehicle.height()
        picture_width=photo_vehicle.width()             
        center_img.place(x=(self.screen_width-picture_width)/2,y=(self.screen_height-picture_height)/2)  
        
        center_img.place(x=(self.screen_width-picture_width)/2,y=(self.screen_height-picture_height)/2)  

        self.main_frame=tk.Frame(self.root,bg='')
        
        label_usfl=tk.Label(self.main_frame,textvariable=self.text_usfl,bg='white',font=("Courier", int(24*self.sf)),fg='black',anchor="center")
        label_usfl.place(x=((self.screen_width-picture_width)/2)-50*self.rw,y=((self.screen_height-picture_height)/2)+150*self.rh)


        label_usfr=tk.Label(self.main_frame,textvariable=self.text_usfr,bg='white',font=("Courier", int(24*self.sf)),fg='black')
        label_usfr.place(x=((self.screen_width-picture_width)/2)+440*self.rw,y=((self.screen_height-picture_height)/2)+150*self.rh)

        label_usbl=tk.Label(self.main_frame,textvariable=self.text_usbl,bg='white',font=("Courier", int(24*self.sf)),fg='black')
        label_usbl.place(x=((self.screen_width-picture_width)/2)-50*self.rw,y=((self.screen_height-picture_height)/2)+750*self.rh)

        label_usbr=tk.Label(self.main_frame,textvariable=self.text_usbr,bg='white',font=("Courier", int(24*self.sf)),fg='black')
        label_usbr.place(x=((self.screen_width-picture_width)/2)+440*self.rw,y=((self.screen_height-picture_height)/2)+750*self.rh)

        label_rpm=tk.Label(self.main_frame,textvariable=self.text_rpm,bg='white',font=("Courier", int(32*self.sf)),fg='black')
        label_rpm.place(x=(self.screen_width/2)-100*self.rw,y=80*self.rh)
 
        label_Time=tk.Label(self.root,textvariable=self.text_time,bg='white',font=("Courier", int(28*self.sf)),fg='black')
        label_Time.place(x=5*self.rw,y=5*self.rh)

        dummypixel = tk.PhotoImage(width=1, height=1)        
        self.button_relay=tk.Button(self.root,image=dummypixel,height=int(100*self.rh),width=int(350*self.rw),text="Start Car",command=self.toggle_car,activebackground="black",bg='#009688',font=("Courier", int(42*self.sf)),activeforeground='white',fg='white',bd=0,justify='center', highlightthickness=0,compound='c')
        self.button_relay.place(x=self.screen_width-360*self.rw,y=0)

        self.update_time()
        self.root.mainloop()


    def toggle_car(self):
        if self.car_running:
            #self.ar_0.senddata('x')
            self.relay_pin.off()
            self.button_relay.config(text="Start Car",activebackground="black",bg='#009688')
            self.car_running=False
            self.main_frame.pack_forget()

        else:
            #self.ar_0.senddata('o')
            self.relay_pin.on()
            self.button_relay.config(text="Stop Car",activebackground="black",bg='#ff6347')
            self.car_running=True
            self.main_frame.pack(fill='both',expand=True)
            self.updateall()

    def updateall(self):
        #self.check_start_condition()
        self.update_ar_0()
        #self.update_ar_1()
        self.update_ar_2()
        if(self.car_running):
            self.root.after(10,self.updateall)

    def check_start_condition(self):
        sensdata=self.ar_0.get_data()

    def update_ar_0(self):
        sensdata=self.ar_0.getcurr_data()
        self.text_rpm.set(sensdata['psrpm']+" rpm")

    def update_ar_2(self):
        sensdata=self.ar_2.getcurr_data()
        if(int(sensdata['usfld'])<300):
            self.text_usfl.set(sensdata['usfld'])
        else:
            self.text_usfl.set(" "*3)
        
        if(int(sensdata['usfrd'])<300):
            self.text_usfr.set(sensdata['usfrd'])
        else:
            self.text_usfr.set(" "*3)

        if(int(sensdata['usbld'])<300):
            self.text_usbl.set(sensdata['usbld'])
        else:
            self.text_usbl.set(" "*3)
        
        if(int(sensdata['usbrd'])<300):
            self.text_usbr.set(sensdata['usbrd'])
        else:
            self.text_usbr.set(" "*3)
        
    
    def update_ar_3(self):
        sensdata=self.ar_3.getcurr_data()
        if(int(sensdata['usbld'])<300):
            self.text_usbl.set(sensdata['usbld'])
        else:
            self.text_usbl.set(" "*3)
        
        if(int(sensdata['usbrd'])<300):
            self.text_usbr.set(sensdata['usbrd'])
        else:
            self.text_usbr.set(" "*3)
    
    
    def update_time(self):
        self.text_time.set(time.strftime("%I:%M %p",time.localtime()))
        self.root.after(100,self.update_time)