import tkinter as tk
import serial
import time
import os
from threading import Thread,Timer
from PIL import ImageTk

class Arduino:
    def __init__(self,device):
        self.device=device

    def getdata(self):
        #self.device.reset_input_buffer()
        time.sleep(0.01)
        final_data={}
        data=self.device.readline().decode().strip().strip('\x00')
        print(data)
        sensdata=data.split("|")
        for s in sensdata:
            t=s.split(":")
            t[1]=" "*(3-len(t[1]))+t[1]
            final_data[t[0]]=t[1]
        return final_data
    
    def senddata(self,data):
        self.device.write(data.encode())