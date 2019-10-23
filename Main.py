from urllib import request
from urllib import error
from time import sleep
from random import randint
from ConError import ConError
from datetime import datetime, timedelta
import socket
import threading
from Alarm import Alarm


class Main(threading.Thread):
    internet_status = ""
    current_time = ""
    last_dc = ""
    start_time = ""
    total_dc = ""
    next_dc = ""
    dc_list = []

    def __init__(self):
        Main.dc_list.append(ConError(date=datetime(year=2019, month=10, day=20, hour=10, minute=38, second=38)))
        Main.dc_list.append(ConError(date=datetime(year=2019, month=10, day=21, hour=4, minute=42, second=0)))
        Main.dc_list.append(ConError(date=datetime(year=2019, month=10, day=21, hour=22, minute=44, second=38)))
        Main.dc_list.append(ConError(date=datetime(year=2019, month=10, day=22, hour=16, minute=47, second=27)))
        threading.Thread.__init__(self)

    def run(self):
        Main.start_time = '{:.19}'.format(str(datetime.now()))

        ip_addresses = ["216.58.192.142", "aftonbladet.se", "mixer.com"]

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

            if len(Main.dc_list) >= 4:
                Main.next_dc = Main.dc_list[-4].time + timedelta(days=3) + timedelta(minutes=11)

            if not Main.internet_status:
                sleep(600)
            else:
                Alarm(self.dc_list)
                sleep(randint(7, 30))
