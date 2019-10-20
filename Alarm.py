from datetime import datetime, timedelta
from pushsafer import init, Client


class Alarm:
    sixty_played = False
    thirty_played = False
    five_played = False

    @staticmethod
    def reset_played_status():
        Alarm.sixty_played = False
        Alarm.thirty_played = False
        Alarm.five_played = False

    def __init__(self, dc_list):
        init("qQUde1zemdqdV5iZFACz")
        self.dc_list = dc_list

        time_to_dc = self.next_dc() - datetime.now()
        time_to_dc = divmod(time_to_dc.seconds, 60)[0]

        if 30 < time_to_dc <= 60 and not Alarm.sixty_played:
            self.push_notification(60)
            Alarm.reset_played_status()
            Alarm.sixty_played = True
        elif 5 < time_to_dc <= 30 and not Alarm.thirty_played:
            self.push_notification(30)
            Alarm.reset_played_status()
            Alarm.thirty_played = True
        elif 0 < time_to_dc <= 5 and not Alarm.five_played:
            self.push_notification(5)
            Alarm.reset_played_status()
            Alarm.five_played = True

    def push_notification(self, time):
        push_title = str(time) + " min to DC!"
        Client("").send_message(message="You will disconnect soon!", title=push_title, device="a", icon="1", sound="0", vibration="1",
                                url="http://192.168.0.142:5000/", urltitle="Tojvoroid", time2live="0", priority="0",
                                retry="0",
                                expire="0", answer="0", picture1="0", picture2="0", picture3="0")

    def next_dc(self):
        if len(self.dc_list) >= 4:
            critical_dc = self.dc_list[-4]
            return critical_dc.time + timedelta(days=3) + timedelta(minutes=11)
        else:
            return datetime(year=2500, month=1, day=1, hour=1, minute=1, second=1)
