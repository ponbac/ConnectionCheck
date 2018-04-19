from urllib import request
from urllib import error
from time import sleep
from random import randint
from con_error import con_error
from datetime import datetime

start_time = str(datetime.now())
print("--Connection checker--")


def internet_on():
    try:
        request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except error.URLError as err:
        con_error()
        return False

while True:
    internet_status = internet_on()
    print("Internet Connection: " + str(internet_status))
    print("Time: " + str(datetime.now()))
    print("Last DC: " + str(con_error.last_dc))
    print("Total disconnects since " + start_time + ": " + str(con_error.total_dc) + "\n")

    if internet_status == False:
        sleep(300)
    else:
        sleep(randint(7, 30))

