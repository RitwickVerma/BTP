import serial
import os
import time

def handshake(devlist):
    devices=os.listdir("/dev")
    for dev in devices:
        if dev[0:6]=="ttyUSB" or dev[0:6]=="ttyACM":
            arduino=serial.Serial("/dev/" + str(dev),9600,timeout=10)
            time.sleep(1)
            arduino.flushInput()
            id=int(arduino.readline().decode().strip().strip('\x00'))
            print(id)
            devlist[id]=arduino
            arduino.write(b'x')   

def shutdown(devlist):
    for arduino in devlist:
        arduino.setDTR(False)
        arduino.setDTR(True)