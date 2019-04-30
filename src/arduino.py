import time

import src.data_god as db

from threading import Thread


class Arduino:
    def __init__(self, device):
        self.device = device
    
    def start_reading(self):
        t = Thread(target=self.thread)
        t.start()
    
    def thread(self):
        run = True
        while run:
            run=self.update_data()
        print("end")

    def update_data(self):
        print('hi')
        if(not self.device.is_open):
            return False
        
        data = self.receive_data_line()
        # print(data)
        sensdata = data.split("|")
        for s in sensdata:
            t = s.split(":")
            t[1] = " " * (3 - len(t[1])) + t[1]
            db.put(t[0], t[1])
        
        time.sleep(0.01)

        return True

    def receive_data_line(self):
        data=self.device.readline().decode().strip().strip('\x00')
        return data

    def send_data(self, data):
        self.device.write(data.encode())
