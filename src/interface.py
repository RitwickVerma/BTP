import os
import tkinter as tk
from PIL import ImageTk, Image

import src.data_god as db

class Interface:
    def __init__(self, relay_pin):
        self.root = tk.Tk()
        self.root.attributes('-zoomed', True)
        self.root.configure(bg='white')
        
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        normal_width = 1920
        normal_height = 1080
        self.rw = self.screen_width / normal_width
        self.rh = self.screen_height / normal_height
        self.sf = ((self.rw + self.rh) / 2)
        self.car_running = False

        self.hotplug = False
        self.relay_pin = relay_pin

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

        self.root.mainloop()

    def update_all(self):
        self.check_start_condition()
        
        self.text_rpm.set(db.get('hsrpm') + " rpm")
        self.text_rpm.set(db.get('hsspeed') + " m/s")
        self.text_rpm.set(db.get('hsdist') + " m")
        self.text_battemp.set("Battery Temperature: " + db.get("dhtt") + " C")
        self.text_bathum.set("Battery Humidity: " + db.get("dhth") + " %")
        self.text_pantemp.set("Solar Panel Temperature: " + db.get("tct") + " C")

        self.text_batvol.set("Battery Voltage: " + db.get("vsbat") + " V")
        self.text_batcurr.set("Battery Current: " + db.get("csbat") + " mA")
        self.text_panvol.set("Solar Panel Voltage: " + db.get("vspan") + " V")
        self.text_pancurr.set("Solar Panel Current: " + db.get("cspan") + " mA")


        if (int(db.get('usld')) < 300):
            self.text_usleft.set(db.get('usld'))
        else:
            self.text_usleft.set(" " * 3)

        if (int(db.get('usrd')) < 300):
            self.text_usright.set(db.get('usrd'))
        else:
            self.text_usright.set(" " * 3)

        if (int(db.get('usbd')) < 300):
            self.text_usback.set(db.get('usbd'))
        else:
            self.text_usback.set(" " * 3)

        self.text_time.set(db.get('time'))
        self.text_cputemp.set("CPU Temperature: " + db.get('cputemp') + " C")
        self.text_lat.set("Latitude: " + str(db.get('lat')))	
        self.text_lon.set("Longitude: " + str(db.get('lon')))



        self.root.after(10, self.update_all)


    def check_start_condition(self):
        if ((db.get("psseated").strip() == "1" and db.get("bsbelt").strip() == "1") or self.hotplug):
            if(not self.car_running):
                self.car_turn_on()
        else:
            if(self.car_running):
                self.car_turn_off()


    def car_turn_on(self):
        self.relay_pin.on()
        self.button_relay.config(text="CAR ON", activebackground="black", bg='#ff6347')
        self.car_running = True
        db.set('carrun', self.car_running)
        self.main_frame.pack(fill='both', expand=True)

    def car_turn_off(self):
        self.relay_pin.off()
        self.button_relay.config(text="CAR OFF", activebackground="black", bg='#009688')
        self.car_running = False
        db.set('carrun', self.car_running)
        self.main_frame.pack_forget()
    
    def car_toggle(self):
        if self.car_running:
            self.car_turn_off()
        else:
            self.car_turn_on()