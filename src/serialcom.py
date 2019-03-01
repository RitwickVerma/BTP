import tkinter as tk
import serial
import time
import os
from threading import Thread,Timer
from PIL import ImageTk
from src.arduino import Arduino
from queue import Queue

class Serialcom():
    def __init__(self,ardlist):
        self.ardlist=ardlist
        
    
    def startreadingserial(self):
        for ard in self.ardlist:
            #q=self.mainbuf[i]
            t=Thread(target=self.ardserial,args=(ard,))
            t.start()

    def ardserial(self,ard):
        while True:
            ard.getdata()

