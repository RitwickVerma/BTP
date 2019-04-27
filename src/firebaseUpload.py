from threading import Thread
import time
import os
from firebase import firebase
import requests

IPDATA_API_KEY="d5b32555042a79b7c7878736419fff91a2e08896a53afda0b4162c7c"

class FirebaseUpload:

    def __init__(self, ardlist):
        self.ardlist = ardlist
        self.update_coordinates()
        self.base = firebase.FirebaseApplication('https://solardatacollection.firebaseio.com/', None)

    def uploadData(self):
        # 1 in cabin
        # 2 volt curr
        # 3 ultrason
        while True:
            time.sleep(5)

            loadBattery = self.base.post('/LoadBattery', {'Time': time.ctime(), 'BatteryTemperature': str(self.ardlist[0].get("dhtt")), 'BatteryCurrent': self.ardlist[1].get("csbat"), 'BatteryVoltage': self.ardlist[1].get("vsbat") })
            print(loadBattery)

            solarPanel = self.base.post('/SolarPanel', {'Time': time.ctime(), 'SolarTemperature': self.ardlist[0].get("tct"), 'SolarCurrent': self.ardlist[1].get("cspan"), 'SolarVoltage': self.ardlist[1].get("vspan") })
            print(solarPanel)

            systemStats = self.base.post('/SystemStats', {'Time': time.ctime(), 'CPUTemperature': self.get_temp(), 'Latitude': self.lat, 'Longitude': self.lon, 'Humidity': str(self.ardlist[0].get("dhth")) })
            print(systemStats)

            self.update_coordinates()            
            

    def startreadingserial(self):
        t = Thread(target=self.uploadData)
        t.start()
        
    def get_temp(self):
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("temp=","").strip()
        temp = temp.replace("'C","")
        return temp

    def update_coordinates(self):
        try:
            r = requests.get('https://api.ipdata.co?api-key='+IPDATA_API_KEY).json()
            self.lat = str(r['latitude'])
            self.lon = str(r['longitude'])

        except requests.ConnectionError:
            self.lat = " "
            self.lon = " "
