import tkinter as tk
import time
from gpiozero import LED
from threading import Thread, Timer

from src.firebaseUpload import FirebaseUpload
from src.interface import Interface
from src.basicFunctions import handshake, shutdown
from src.serialCom import Serialcom


def main():
    pass
    ardlist = handshake()

    serialcom = Serialcom(ardlist)
    serialcom.startreadingserial()

    fb = FirebaseUpload(ardlist)
    fb.startreadingserial()
    relay_pin=LED(3)
    relay_pin.off()
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='white')

    interf = Interface(root, ardlist, relay_pin)
    interf.guiloop()

    shutdown(ardlist, relay_pin)


if __name__ == "__main__":
    main()
