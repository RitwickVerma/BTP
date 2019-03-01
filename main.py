import tkinter as tk
import time
from threading import Thread,Timer

from src.interface import Interface
from src.basefuncs import handshake,shutdown
from src.serialcom import Serialcom


def main():
    devlist=[None,None,None,None]
    ardlist=handshake(devlist)

    serialcom=Serialcom(ardlist)
    serialcom.startreadingserial()
    #data_thread=Thread(target=serialcom.startreadingserial)
    #data_thread.start()


    root=tk.Tk()
    root.attributes('-zoomed', True)
    root.configure(bg='white') 

    interf=Interface(root,ardlist)
    interf.guiloop()
    
    shutdown(ardlist)

if __name__ == "__main__":
    main()