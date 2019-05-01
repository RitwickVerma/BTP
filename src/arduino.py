import time

import src.data_god as db

from threading import Thread

class Arduino:
    def __init__(self, device):
        self.device = device
    
    def start_reading(self):
        t = Thread(target=self.update_data)
        t.start()
    
    def update_data(self):
        while db.get_prog_running():          
            data = self.receive_data_line()
            print(data)
            sensdata = data.split("|")
            for s in sensdata:
                t = s.split(":")
                t[1] = " " * (3 - len(t[1])) + t[1]
                db.set(t[0], t[1])
            
            time.sleep(0.01)


    def receive_data_line(self):
        data=self.device.readline().decode().strip().strip('\x00')
        return data

    def send_data(self, data):
        self.device.write(data.encode())
