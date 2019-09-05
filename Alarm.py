from playsound import playsound
from datetime import datetime, timedelta


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
        self.dc_list = dc_list

        time_to_dc = self.next_dc() - datetime.now()
        time_to_dc = divmod(time_to_dc.seconds, 60)[0]

        if 30 < time_to_dc <= 60 and not Alarm.sixty_played:
            self.play(60)
            Alarm.reset_played_status()
            Alarm.sixty_played = True
        elif 5 < time_to_dc <= 30 and not Alarm.thirty_played:
            self.play(30)
            Alarm.reset_played_status()
            Alarm.thirty_played = True
        elif 0 < time_to_dc <= 5 and not Alarm.five_played:
            self.play(5)
            Alarm.reset_played_status()
            Alarm.five_played = True

    def play(self, time):
        playsound("sounds/" + str(time) + "min.mp3")

    def next_dc(self):
        if len(self.dc_list) >= 4:
            critical_dc = self.dc_list[-4]
            return critical_dc.time + timedelta(days=3) + timedelta(minutes=15)
        else:
            return datetime(year=2500, month=1, day=1, hour=1, minute=1, second=1)
