from datetime import datetime


class ConError:

    total_dc = 0
    last_dc = "Never"

    def __init__(self):
        ConError.last_dc = datetime.now()
        ConError.total_dc += 1

        self.time = datetime.now()
