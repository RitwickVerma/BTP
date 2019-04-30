from threading import Thread
from firebase import firebase
import time

import src.data_god as db


class FirebaseUpload:

    def __init__(self, ardlist):
        self.base = firebase.FirebaseApplication('https://solardatacollection.firebaseio.com/', None)

    def start_uploading(self):
        t = Thread(target=self.upload_data)
        t.start()

    def upload_data(self):
        while True:
            time.sleep(5)

            loadBattery = self.base.post('/LoadBattery', {'Time': db.get('time'), 'BatteryTemperature': str(db.get("dhtt")), 'BatteryCurrent': db.get("csbat"), 'BatteryVoltage': db.get("vsbat") })
            print(loadBattery)

            solarPanel = self.base.post('/SolarPanel', {'Time': time.ctime(), 'SolarTemperature': db.get("tct"), 'SolarCurrent': db.get("cspan"), 'SolarVoltage': db.get("vspan") })
            print(solarPanel)

            systemStats = self.base.post('/SystemStats', {'Time': time.ctime(), 'CPUTemperature': db.get('cputemp'), 'Latitude': db.get('lat'), 'Longitude': db.get('lon'), 'Humidity': str(db.get("dhth")) })
            print(systemStats)
