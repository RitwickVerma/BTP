import tkinter as tk
import serial
import time
import os
from threading import Thread, Event
from PIL import ImageTk
from src.arduino import Arduino
from queue import Queue


class Serialcom:
    def __init__(self, ardlist):
        self.ardlist = ardlist

    def startreadingserial(self):
        for ard in self.ardlist:
            if (ard != None):
                t = Thread(target=self.ardserialthread, args=(ard,))
                t.start()

    def ardserialthread(self, ard):
        while True:
            ard.getdata()
