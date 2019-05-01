import time
import serial
from src.arduino import Arduino
from src.firebase import FirebaseUpload
from src.interface import Interface
import src.misc_data as misc
import src.data_god as db


import os

if(os.uname()[1]=='raspberrypi'):
    from gpiozero import LED

def main():
    startup()

    if(os.uname()[1]=='raspberrypi'):
        relay_pin = LED(3)
        relay_pin.off()
    else:
        class dummy_relay:
            def on(self):
                pass
            def off(self):
                pass
        relay_pin = dummy_relay()

    misc.start_updating()

    firebase = FirebaseUpload()
    firebase.start_uploading()

    interface = Interface(relay_pin)
    interface.guiloop()

    shutdown(relay_pin)

def startup():
    db.set_prog_running(True)
    devices = os.listdir("/dev")
    for dev in devices:
        if dev[0:6] == "ttyUSB" or dev[0:6] == "ttyACM":
            arduino_com = serial.Serial("/dev/" + str(dev), 9600, timeout=10)
            time.sleep(0.1)
            arduino_com.flushInput()
            arduino = Arduino(arduino_com)
            arduino.start_reading()


def shutdown(relay_pin):
    relay_pin.off()
    db.set_prog_running(False)

if __name__ == "__main__":
    main()
