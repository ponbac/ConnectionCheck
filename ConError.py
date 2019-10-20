from datetime import datetime


class ConError:
    total_dc = 0
    last_dc = "Never"

    def __init__(self, time=datetime.now()):
        ConError.last_dc = time
        ConError.total_dc += 1

        self.time = time
