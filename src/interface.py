import tkinter as tk
import serial
import time
import os
import requests
from queue import Queue
from PIL import ImageTk, Image
from src.arduino import Arduino

IPDATA_API_KEY="d5b32555042a79b7c7878736419fff91a2e08896a53afda0b4162c7c"

class Interface:
    def __init__(self, root, ardlist, relay_pin):
        self.root = root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        normal_width = 1920
        normal_height = 1080
        self.rw = self.screen_width / normal_width
        self.rh = self.screen_height / normal_height
        self.sf = ((self.rw + self.rh) / 2)
        self.car_running = False

        self.relay_pin = relay_pin
        self.ar_0 = ardlist[0]
        self.ar_1 = ardlist[1]
        self.ar_2 = ardlist[2]

    def guiloop(self):

        self.text_usleft = tk.StringVar(self.root)
        self.text_usright = tk.StringVar(self.root)
        self.text_usback = tk.StringVar(self.root)
        self.text_time = tk.StringVar(self.root)
        self.text_rpm = tk.StringVar(self.root)
        self.text_speed = tk.StringVar(self.root)
        self.text_distance = tk.StringVar(self.root)
        self.text_batvol = tk.StringVar(self.root)
        self.text_batcurr = tk.StringVar(self.root)
        self.text_panvol = tk.StringVar(self.root)
        self.text_pancurr = tk.StringVar(self.root)
        self.text_battemp = tk.StringVar(self.root)
        self.text_bathum = tk.StringVar(self.root)
        self.text_pantemp = tk.StringVar(self.root)
        self.text_cputemp = tk.StringVar(self.root)
        self.text_lat = tk.StringVar(self.root)
        self.text_lon = tk.StringVar(self.root)

        photo_vehicle = Image.open(os.path.dirname(os.path.realpath(__file__)) + "/img_res/car.png")
        photo_vehicle = photo_vehicle.resize((int(self.screen_width * 0.25), int(self.screen_height * 0.75)),
                                             Image.ANTIALIAS)
        photo_vehicle = ImageTk.PhotoImage(photo_vehicle)
        center_img = tk.Label(self.root, image=photo_vehicle, relief='flat', bg='white')
        center_img.image = photo_vehicle
        picture_height = photo_vehicle.height()
        picture_width = photo_vehicle.width()
        center_img.place(x=(self.screen_width - picture_width) / 2,
                         y=(self.screen_height - picture_height) / 2 - 50 * self.rh)

        self.main_frame = tk.Frame(self.root, bg='')
        # self.main_frame.pack(fill='both', expand=True)

        label_usleft = tk.Label(self.main_frame, textvariable=self.text_usleft, bg='white',
                              font=("Courier", int(24 * self.sf)), fg='black', anchor="center")
        label_usleft.place(x=((self.screen_width - picture_width) / 2) - 50 * self.rw,
                         y=((self.screen_height) / 2) - 100 * self.rh)

        label_usright = tk.Label(self.main_frame, textvariable=self.text_usright, bg='white',
                              font=("Courier", int(24 * self.sf)), fg='black')
        label_usright.place(x=((self.screen_width - picture_width) / 2) + 440 * self.rw,
                         y=((self.screen_height) / 2) - 100 * self.rh)

        label_usback = tk.Label(self.main_frame, textvariable=self.text_usback, bg='white',
                              font=("Courier", int(24 * self.sf)), fg='black')
        label_usback.place(x=((self.screen_width) / 2) - 50 * self.rw,
                         y=((self.screen_height)) - 150 * self.rh)


        label_rpm = tk.Label(self.main_frame, textvariable=self.text_rpm, bg='white',
                             font=("Courier", int(32 * self.sf)), fg='black')
        # label_rpm.place(x=(self.screen_width) - 400 * self.rw, y=self.screen_height / 2 - 200 * self.rh)

        label_speed = tk.Label(self.main_frame, textvariable=self.text_speed, bg='white',
                             font=("Courier", int(32 * self.sf)), fg='black')
        # label_speed.place(x=(self.screen_width) - 400 * self.rw, y=self.screen_height / 2 - 150 * self.rh)

        label_distance = tk.Label(self.main_frame, textvariable=self.text_distance, bg='white',
                             font=("Courier", int(32 * self.sf)), fg='black')
        # label_distance.place(x=(self.screen_width) - 400 * self.rw, y=self.screen_height / 2 - 100 * self.rh)



        label_stathead = tk.Label(self.main_frame, text="Car stats", bg='white',
                              font=("Courier", int(22 * self.sf)), fg='#ff6347', anchor="center")
        label_stathead.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 50 * self.rh)

        label_batvol = tk.Label(self.main_frame, textvariable=self.text_batvol, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_batvol.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 100 * self.rh)

        label_batcurr = tk.Label(self.main_frame, textvariable=self.text_batcurr, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_batcurr.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 130 * self.rh)

        label_panvol = tk.Label(self.main_frame, textvariable=self.text_panvol, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_panvol.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 160 * self.rh)

        label_pancurr = tk.Label(self.main_frame, textvariable=self.text_pancurr, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_pancurr.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 190 * self.rh)

        label_battemp = tk.Label(self.main_frame, textvariable=self.text_battemp, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_battemp.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 220 * self.rh)

        label_bathum = tk.Label(self.main_frame, textvariable=self.text_bathum, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_bathum.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 250 * self.rh)

        label_pantemp = tk.Label(self.main_frame, textvariable=self.text_pantemp, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_pantemp.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 280 * self.rh)

        label_cputemp = tk.Label(self.main_frame, textvariable=self.text_cputemp, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_cputemp.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 310 * self.rh)

        label_lat = tk.Label(self.main_frame, textvariable=self.text_lat, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_lat.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 340 * self.rh)

        label_lon = tk.Label(self.main_frame, textvariable=self.text_lon, bg='white',
                              font=("Courier", int(14 * self.sf)), fg='black', anchor="center")
        label_lon.place(x=50 * self.rw,
                         y=((self.screen_height) / 2) + 370 * self.rh)



        label_Time = tk.Label(self.root, textvariable=self.text_time, bg='white', font=("Courier", int(28 * self.sf)),
                              fg='black')
        label_Time.place(x=5 * self.rw, y=5 * self.rh)

        dummypixel = tk.PhotoImage(width=1, height=1)
        self.button_relay = tk.Label(self.root, image=dummypixel, height=int(100 * self.rh), width=int(350 * self.rw),
                                      text="CAR OFF", activebackground="black", bg='#009688',
                                      font=("Courier", int(42 * self.sf)), activeforeground='white', fg='white', bd=0,
                                      justify='center', highlightthickness=0, compound='c')
        self.button_relay.place(x=self.screen_width - 340 * self.rw, y=0)


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
        self.button_relay.config(text="CAR ON", activebackground="black", bg='#ff6347')
        self.car_running = True
        self.main_frame.pack(fill='both', expand=True)

    def car_turn_off(self):
        self.relay_pin.off()
        self.button_relay.config(text="CAR OFF", activebackground="black", bg='#009688')
        self.car_running = False
        self.main_frame.pack_forget()

    def update_all(self):
        self.check_start_condition()
        self.update_ar_0()
        self.update_ar_1()
        self.update_ar_2()
        self.update_rest()
        self.root.after(10, self.update_all)

    def check_start_condition(self):
        if (self.ar_0.get("psseated").strip() == "1" and self.ar_0.get("bsbelt").strip() == "1"):
            if(not self.car_running):
                self.car_turn_on()
        else:
            if(self.car_running):
                self.car_turn_off()

    def update_ar_0(self):
        self.text_rpm.set(self.ar_0.get('hsrpm') + " rpm")
        self.text_rpm.set(self.ar_0.get('hsspeed') + " m/s")
        self.text_rpm.set(self.ar_0.get('hsdist') + " m")
        self.text_battemp.set("Battery Temperature: " + self.ar_0.get("dhtt") + " C")
        self.text_bathum.set("Battery Humidity: " + self.ar_0.get("dhth") + " %")
        self.text_pantemp.set("Solar Panel Temperature: " + self.ar_0.get("tct") + " C")

    def update_ar_1(self):
        self.text_batvol.set("Battery Voltage: " + self.ar_1.get("vsbat") + " V")
        self.text_batcurr.set("Battery Current: " + self.ar_1.get("csbat") + " mA")
        self.text_panvol.set("Solar Panel Voltage: " + self.ar_1.get("vspan") + " V")
        self.text_pancurr.set("Solar Panel Current: " + self.ar_1.get("cspan") + " mA")

    def update_ar_2(self):
        if (int(self.ar_2.get('usld')) < 300):
            self.text_usleft.set(self.ar_2.get('usld'))
        else:
            self.text_usleft.set(" " * 3)

        if (int(self.ar_2.get('usrd')) < 300):
            self.text_usright.set(self.ar_2.get('usrd'))
        else:
            self.text_usright.set(" " * 3)

        if (int(self.ar_2.get('usbd')) < 300):
            self.text_usback.set(self.ar_2.get('usbd'))
        else:
            self.text_usback.set(" " * 3)

    def update_rest(self):
        self.text_cputemp.set("CPU Temperature: " + self.get_temp() + "C")

    def update_time(self):
        self.text_time.set(time.strftime("%I:%M %p", time.localtime()))
        self.root.after(100, self.update_time)

    def update_coordinates(self):
        try:
            r = requests.get('https://api.ipdata.co?api-key='+IPDATA_API_KEY).json()
            self.text_lat.set("Latitude: " + str(r['latitude']))
            self.text_lon.set("Longitude: " + str(r['longitude']))
        except requests.ConnectionError:
            self.text_lat.set("")
            self.text_lon.set("")

        self.root.after(5000, self.update_coordinates)

    def get_temp(self):
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("temp=","").strip()
        temp = temp.replace("'C","")
        return temp
