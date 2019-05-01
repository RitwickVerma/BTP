from threading import Thread
import requests
import os
import time

import src.data_god as db

def start_updating():
    t = Thread(target=update_coordinates)
    t.start()

    t = Thread(target=update_temp)
    t.start()

    t = Thread(target=update_time)
    t.start()

def update_misc():
    update_coordinates()
    update_temp()


def update_coordinates():
    while db.get_prog_running():
        try:
            r = requests.get('https://api.ipdata.co?api-key='+db.get('API_KEY')).json()
            db.set('lat',r['latitude'])
            db.set('lon',r['longitude'])
        except requests.ConnectionError:
            db.set('lat','Internet disconnected')
            db.set('lon','Internet disconnected')
            
        time.sleep(5)


def update_temp():
    while db.get_prog_running():
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("temp=","").strip()
        temp = temp.replace("'C","")
        db.set('cputemp',temp)

        time.sleep(0.5)

def update_time():
    while db.get_prog_running():
        db.set('time',time.strftime("%I:%M %p", time.localtime()))
        time.sleep(0.5)
