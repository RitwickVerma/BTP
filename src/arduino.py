import tkinter as tk
import serial
import time
import os
from threading import Thread, Timer
from PIL import ImageTk


class Arduino:
    def __init__(self, device):
        self.device = device
        self.curr_data = {}

    def getdata(self):
        final_data = {}
        try:
            data = self.device.readline().decode().strip().strip('\x00')
        except:
            return False
        print(data)
        if (len(data) <= 1):
            return False

        sensdata = data.split("|")
        for s in sensdata:
            t = s.split(":")
            t[1] = " " * (3 - len(t[1])) + t[1]
            final_data[t[0]] = t[1]

        self.curr_data = final_data

        return True

    def getcurr_data(self):
        return self.curr_data

    def get(self, key):
        return self.curr_data.get(key, "nil")

    def senddata(self, data):
        self.device.write(data.encode())
