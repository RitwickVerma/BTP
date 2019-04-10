import tkinter as tk
import serial
import time
import os
import requests
from gpiozero import LED
from queue import Queue
from PIL import ImageTk, Image
from src.arduino import Arduino

IPDATA_API_KEY="d5b32555042a79b7c7878736419fff91a2e08896a53afda0b4162c7c"

class Interface:
    def __init__(self, root, ardlist):
        self.root = root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        normal_width = 1920
        normal_height = 1080
        self.rw = self.screen_width / normal_width
        self.rh = self.screen_height / normal_height
        self.sf = ((self.rw + self.rh) / 2)
        self.car_running = False

        self.relay_pin=LED(3)
        self.ar_0 = ardlist[0]
        self.ar_1 = ardlist[1]
        self.ar_2 = ardlist[2]

    def guiloop(self):

        self.text_usfl = tk.StringVar(self.root)
        self.text_usfr = tk.StringVar(self.root)
        self.text_usbl = tk.StringVar(self.root)
        self.text_usbr = tk.StringVar(self.root)
        self.text_time = tk.StringVar(self.root)
        self.text_rpm = tk.StringVar(self.root)
        self.text_vsbat = tk.StringVar(self.root)
        self.text_csbat = tk.StringVar(self.root)
        self.text_vspan = tk.StringVar(self.root)
        self.text_cspan = tk.StringVar(self.root)
        self.text_lat = tk.StringVar(self.root)
        self.text_lon = tk.StringVar(self.root)

        photo_vehicle = Image.open(os.path.dirname(os.path.realpath(__file__)) + "/img_res/car.png")
        photo_vehicle = photo_vehicle.resize((int(self.screen_width * 0.25), int(self.screen_height * 0.75)),
                                             Image.ANTIALIAS)
        photo_vehicle = ImageTk.PhotoImage(photo_vehicle)
        center_img = tk.Label(self.root, image=photo_vehicle, relief='flat', bg='black')
        center_img.image = photo_vehicle
        picture_height = photo_vehicle.height()
        picture_width = photo_vehicle.width()
        center_img.place(x=(self.screen_width - picture_width) / 2, y=(self.screen_height - picture_height) / 2)

        self.main_frame = tk.Frame(self.root, bg='')
        self.main_frame.pack(fill='both', expand=True)

        label_usfl = tk.Label(self.main_frame, textvariable=self.text_usfl, bg='white',
                              font=("Courier", int(24 * self.sf)), fg='black', anchor="center")
        label_usfl.place(x=((self.screen_width - picture_width) / 2) - 50 * self.rw,
                         y=((self.screen_height - picture_height) / 2) + 150 * self.rh)

        label_usfr = tk.Label(self.main_frame, textvariable=self.text_usfr, bg='white',
                              font=("Courier", int(24 * self.sf)), fg='black')
        label_usfr.place(x=((self.screen_width - picture_width) / 2) + 440 * self.rw,
                         y=((self.screen_height - picture_height) / 2) + 150 * self.rh)

        label_usbl = tk.Label(self.main_frame, textvariable=self.text_usbl, bg='white',
                              font=("Courier", int(24 * self.sf)), fg='black')
        label_usbl.place(x=((self.screen_width - picture_width) / 2) - 50 * self.rw,
                         y=((self.screen_height - picture_height) / 2) + 750 * self.rh)

        label_usbr = tk.Label(self.main_frame, textvariable=self.text_usbr, bg='white',
                              font=("Courier", int(24 * self.sf)), fg='black')
        label_usbr.place(x=((self.screen_width - picture_width) / 2) + 440 * self.rw,
                         y=((self.screen_height - picture_height) / 2) + 750 * self.rh)

        label_rpm = tk.Label(self.main_frame, textvariable=self.text_rpm, bg='white',
                             font=("Courier", int(32 * self.sf)), fg='black')
        label_rpm.place(x=(self.screen_width / 2) - 80 * self.rw, y=60 * self.rh)



        label_stathead = tk.Label(self.main_frame, text="Car stats", bg='white',
                              font=("Courier", int(22 * self.sf)), fg='#ff6347', anchor="center")
        label_stathead.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 100 * self.rh)

        label_vsbat = tk.Label(self.main_frame, textvariable=self.text_vsbat, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_vsbat.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 150 * self.rh)

        label_csbat = tk.Label(self.main_frame, textvariable=self.text_csbat, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_csbat.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 180 * self.rh)

        label_vspan = tk.Label(self.main_frame, textvariable=self.text_vspan, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_vspan.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 210 * self.rh)

        label_cspan = tk.Label(self.main_frame, textvariable=self.text_cspan, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_cspan.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 240 * self.rh)

        label_lat = tk.Label(self.main_frame, textvariable=self.text_lat, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_lat.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 270 * self.rh)

        label_lon = tk.Label(self.main_frame, textvariable=self.text_lon, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_lon.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 300 * self.rh)




        label_Time = tk.Label(self.root, textvariable=self.text_time, bg='white', font=("Courier", int(28 * self.sf)),
                              fg='black')
        label_Time.place(x=5 * self.rw, y=5 * self.rh)

        dummypixel = tk.PhotoImage(width=1, height=1)
        self.button_relay = tk.Button(self.root, image=dummypixel, command=self.car_toggle, height=int(100 * self.rh), width=int(350 * self.rw),
                                      text="Start Car", activebackground="black", bg='#009688',
                                      font=("Courier", int(42 * self.sf)), activeforeground='white', fg='white', bd=0,
                                      justify='center', highlightthickness=0, compound='c')
        self.button_relay.place(x=self.screen_width - 360 * self.rw, y=0)

        
        self.update_all()
        self.update_time()
        self.update_coordinates() 

        # self.main_frame.pack_forget()
        self.root.mainloop()


    def car_toggle(self):
        if self.car_running:
            self.car_turn_off()
        else:
            self.car_turn_on()

    def car_turn_on(self):
        self.relay_pin.on()
        self.button_relay.config(text="Stop Car", activebackground="black", bg='#ff6347')
        self.car_running = True
        self.main_frame.pack(fill='both', expand=True)

    def car_turn_off(self):
        self.relay_pin.off()
        self.button_relay.config(text="Start Car", activebackground="black", bg='#009688')
        self.car_running = False
        self.main_frame.pack_forget()

    def update_all(self):
        self.check_start_condition()
        self.update_ar_0()
        self.update_ar_1()
        self.update_ar_2()
        # self.update_coordinates()
        self.root.after(10, self.update_all)

    def check_start_condition(self):
        if (self.ar_0.get("psseated").strip() == "1" and self.ar_0.get("bsbelt").strip() == "1"):
            self.car_turn_on()
        else:
            self.car_turn_off()

    def update_ar_0(self):
        self.text_rpm.set(self.ar_0.get('psrpm') + " rpm")

    def update_ar_1(self):
        self.text_vsbat.set("Battery Voltage: " + self.ar_1.get("vsbat"))
        self.text_csbat.set("Battery Current: " + self.ar_1.get("csbat"))
        self.text_vspan.set("Solar Panel Voltage: " + self.ar_1.get("vspan"))
        self.text_cspan.set("Solar Panel Current: " + self.ar_1.get("cspan"))

    def update_ar_2(self):
        if (int(self.ar_2.get('usfld')) < 300):
            self.text_usfl.set(self.ar_2.get('usfld'))
        else:
            self.text_usfl.set(" " * 3)

        if (int(self.ar_2.get('usfrd')) < 300):
            self.text_usfr.set(self.ar_2.get('usfrd'))
        else:
            self.text_usfr.set(" " * 3)

        if (int(self.ar_2.get('usbld')) < 300):
            self.text_usbl.set(self.ar_2.get('usbld'))
        else:
            self.text_usbl.set(" " * 3)

        if (int(self.ar_2.get('usbrd')) < 300):
            self.text_usbr.set(self.ar_2.get('usbrd'))
        else:
            self.text_usbr.set(" " * 3)

    def update_time(self):
        self.text_time.set(time.strftime("%I:%M %p", time.localtime()))
        self.root.after(100, self.update_time)

    def update_coordinates(self):
        r = requests.get('https://api.ipdata.co?api-key='+IPDATA_API_KEY).json()
        self.text_lat.set("Latitude: " + str(r['latitude']))
        self.text_lon.set("Longitude: " + str(r['longitude']))
        # self.root.after(5000, self.update_coordinates)
