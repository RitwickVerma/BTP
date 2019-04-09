from threading import Thread
import time

from firebase import firebase


class FirebaseUpload:

    def __init__(self, ardlist):
        self.ardlist = ardlist
        self.base = firebase.FirebaseApplication('https://solardatacollection.firebaseio.com/', None)

    def uploadData(self):
        # 1 in cabin
        # 2 volt curr
        # 3 ultrason
        while True:
            result = self.base.post('/Temperature',
                                {'Time': time.ctime(), 'BatteryTemperature': '', 'SolarTemperature': ''})
            time.sleep(10)
            print(result)

    def startreadingserial(self):
       t = Thread(target=self.uploadData())
