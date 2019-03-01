import tkinter as tk
import time
from src.interface import Interface
from src.basefuncs import handshake,shutdown

def main():
    devlist=[None,None,None,None]
    handshake(devlist)
    root=tk.Tk()
    root.attributes('-zoomed', True)
    #root.wm_attributes('-alpha', 1)  
    #root.wm_attributes('-transparentcolor','black')
    root.configure(bg='white') 
    interf=Interface(root,devlist)
    interf.guiloop()
    #root.mainloop()
    shutdown(devlist)

if __name__ == "__main__":
    main()