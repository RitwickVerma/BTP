import tkinter as tk
import time
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

    # fb = FirebaseUpload(ardlist)
    # fb.startreadingserial()
    
    root = tk.Tk()
    root.attributes('-zoomed', True)
    root.configure(bg='white')

    interf = Interface(root, ardlist)
    interf.guiloop()

    shutdown(ardlist)


if __name__ == "__main__":
    main()
