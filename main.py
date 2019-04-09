import tkinter as tk
import time
from threading import Thread,Timer

from src.interface import Interface
from src.basefuncs import handshake,shutdown
from src.serialcom import Serialcom

def main():
    ardlist=handshake()

    serialcom=Serialcom(ardlist)
    serialcom.startreadingserial()

    root=tk.Tk()
    root.attributes('-zoomed', True)
    root.configure(bg='white') 

    interf=Interface(root,ardlist)
    interf.guiloop()
    
    shutdown(ardlist)

if __name__ == "__main__":
    main()