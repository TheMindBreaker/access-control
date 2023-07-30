from urllib.request import urlopen as url
import config

def check_connection():
    try:
        url(config.MAIN_SERVER, timeout=3)
        return True
    except ConnectionError as e: 
        return False

