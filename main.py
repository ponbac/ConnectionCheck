from urllib import request
from urllib import error
from time import sleep
from random import randint
from con_error import con_error
from datetime import datetime
import socket

start_time = str(datetime.now())
print("--Connection checker--")

ip_list = ["216.58.192.142", "aftonbladet.se", "mixer.com", "op.gg", "sundsvall.se"]


def internet_on(address):
    success = False

    for ip in ip_list:
        try:
            request.urlopen("http://" + ip, timeout=2)
            success = True
        except error.URLError as err:
            print("URL that generated the error code: ", ip)
            print("Error description:", err.reason)
        except socket.timeout:
            print("URL that generated the error code: ", ip)
            print("Error description: No response.")
        except socket.error:
            print("URL that generated the error code: ", ip)
            print("Error description: Socket error.")

    if success == False:
        con_error()

    return success

while True:
    internet_status = internet_on(ip_list)
    print("\nInternet Connection: " + str(internet_status))
    print("Time: " + str(datetime.now()))
    print("Last DC: " + str(con_error.last_dc))
    print("Total disconnects since " + start_time + ": " + str(con_error.total_dc) + "\n")

    if internet_status == False:
        sleep(300)
    else:
        sleep(randint(7, 30))

