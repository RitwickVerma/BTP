import serial
import os
import time
from src.arduino import Arduino
from gpiozero import LED


def handshake():
    ardlist = [None, None, None]
    devices = os.listdir("/dev")
    for dev in devices:
        if dev[0:6] == "ttyUSB" or dev[0:6] == "ttyACM":
            arduino = serial.Serial("/dev/" + str(dev), 9600, timeout=10)
            time.sleep(0.1)
            arduino.flushInput()
            id = int(arduino.readline().decode().strip().strip('\x00'))
            print(id)
            # devlist[id]=arduino
            arduino.write(b'x')
            ardlist[id] = Arduino(arduino)
    return ardlist


def shutdown(ardlist, relay_pin):
    relay_pin.off()
    for arduino in ardlist:
        arduino.device.close()
        arduino.device.setDTR(False)
        arduino.device.setDTR(True)
