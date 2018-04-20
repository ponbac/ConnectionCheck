from urllib import request
from urllib import error
from time import sleep
from random import randint
from con_error import con_error
from datetime import datetime

start_time = str(datetime.now())
print("--Connection checker--")

ip_list = ["216.58.192.142", "aftonbladet.se", "chalmers.se", "twitch.com", "sundsvall.se"]


def internet_on(address):
    success = False

    for ip in ip_list:
        try:
            request.urlopen("http://" + ip, timeout=1)
            success = True
        except error.URLError as err:
            print("Could not reach: " + ip)

    if success == False:
        con_error()

    return success

while True:
    internet_status = internet_on(ip_list)
    print("Internet Connection: " + str(internet_status))
    print("Time: " + str(datetime.now()))
    print("Last DC: " + str(con_error.last_dc))
    print("Total disconnects since " + start_time + ": " + str(con_error.total_dc) + "\n")

    if internet_status == False:
        sleep(300)
    else:
        sleep(randint(7, 30))

