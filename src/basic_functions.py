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
            arduino_com = serial.Serial("/dev/" + str(dev), 9600, timeout=10)
            arduino = Arduino(arduino_com)
            time.sleep(0.1)
            arduino_com.flushInput()
            id = int(arduino.receive_data_line())
            print(id)
            arduino.start_reading()
            ardlist[id] = arduino
            # devlist[id]=ardino
            arduino.send_data('x')
    return ardlist


def shutdown(ardlist, relay_pin):
    relay_pin.off()
    for arduino in ardlist:
        arduino.device.close()
        arduino.device.setDTR(False)
        arduino.device.setDTR(True)
