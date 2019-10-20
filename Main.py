from urllib import request
from urllib import error
from time import sleep
from random import randint
from ConError import ConError
from datetime import datetime
import socket
import threading
from Alarm import Alarm


class Main (threading.Thread):

    internet_status = ""
    current_time = ""
    last_dc = ""
    start_time = ""
    total_dc = ""
    dc_list = []

    def __init__(self):
        #Main.dc_list.append(ConError(datetime(year=2019, month=10, day=17, hour=10, minute=26, second=58)))
        #Main.dc_list.append(ConError(datetime(year=2019, month=10, day=18, hour=4, minute=30, second=2)))
        #Main.dc_list.append(ConError(datetime(year=2019, month=10, day=18, hour=22, minute=32, second=56)))
        #Main.dc_list.append(ConError(datetime(year=2019, month=10, day=19, hour=16, minute=36, second=15)))
        threading.Thread.__init__(self)

    def run(self):
        Main.start_time = '{:.19}'.format(str(datetime.now()))

        ip_addresses = ["216.58.192.142", "aftonbladet.se", "mixer.com", "op.gg"]

        def internet_on(ip_list):
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

            if not success:
                Main.dc_list.append(ConError())
                history_file = open('history.txt', 'a+')
                history_file.write('{:.19}'.format(str(datetime.now())) + '\n')
                history_file.close()

            return success

        while True:
            Main.internet_status = internet_on(ip_addresses)
            Main.current_time = '{:.19}'.format(str(datetime.now()))
            Main.last_dc = '{:.19}'.format(str(ConError.last_dc))
            Main.total_dc = str(ConError.total_dc)

            if not Main.internet_status:
                sleep(600)
            else:
                Alarm(self.dc_list)
                sleep(randint(7, 30))



