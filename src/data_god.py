data_god={"API_KEY":"d5b32555042a79b7c7878736419fff91a2e08896a53afda0b4162c7c"}

def set(key, value):
    data_god[key]=value

def get(key):
    try:
        return data_god[key]
    except:
        return '69'

def get_prog_running():
    try:
        return data_god['progrun']
    except:
        return False

def set_prog_running(bool):
    set('progrun',bool)