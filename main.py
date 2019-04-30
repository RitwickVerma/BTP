from src.firebase import FirebaseUpload
from src.interface import Interface
from src.basic_functions import handshake, shutdown
from src.serial_com import SerialCom
import src.misc_data as misc

import os

if(os.uname()[1]=='raspberrypi'):
    from gpiozero import LED

def main():
    pass
    ardlist = handshake()

    # serial_com = SerialCom(ardlist)
    # serial_com.start_reading_serial()
    misc.start_updating()
    # firebase = FirebaseUpload(ardlist)
    # firebase.start_uploading()
    if(os.uname()[1]=='raspberrypi'):
        relay_pin=LED(3)
        relay_pin.off()
    else:
        class dummy_relay:
            def on(self):
                pass
            def off(self):
                pass
        relay_pin = dummy_relay()

    interface = Interface(relay_pin)
    interface.guiloop()

    # shutdown(ardlist, relay_pin)


if __name__ == "__main__":
    main()
