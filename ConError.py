from datetime import datetime

class ConError:

    total_dc = 0
    last_dc = "Never"

    def __init__(self):
        ConError.last_dc = datetime.now()
        ConError.total_dc += 1

    #def time_since_last_dc:
    #    ConError.last_dc.