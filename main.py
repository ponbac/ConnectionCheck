from urllib import request
from urllib import error
from time import sleep
from random import randint
from ConError import ConError
from datetime import datetime
import socket
import threading


class Main (threading.Thread):

    internet_status = ""
    current_time = ""
    last_dc = ""
    start_time = ""
    total_dc = ""

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        Main.start_time = str(datetime.now())
        print("--Connection checker--")

        ip_addresses = ["216.58.192.142", "aftonbladet.se", "mixer.com", "op.gg", "sundsvall.se"]

        def internet_on(self, ip_list):
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
                ConError()

            return success

        while True:
            Main.internet_status = internet_on(self, ip_addresses)
            Main.current_time = str(datetime.now())
            Main.last_dc = str(ConError.last_dc)
            Main.total_dc = str(ConError.total_dc)

            if Main.internet_status == False:
                sleep(300)
            else:
                sleep(randint(7, 30))



