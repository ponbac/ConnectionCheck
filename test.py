import urllib.request
import urllib.error
import time
from random import randint
from ConError import ConError

from datetime import datetime

print("--Connection checker--")


def internet_on():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib.error.URLError as err:
        ConError()
        return False

while True:
    print("Internet Connection: " + str(internet_on()))
    print("Time: " + str(datetime.now()))
    print("Last DC: " + str(ConError.last_dc) + "\n")
    time.sleep(randint(7, 30))

