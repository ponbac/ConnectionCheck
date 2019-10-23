from datetime import datetime


class ConError:
    total_dc = 0
    last_dc = "Never"

    def __init__(self, **keyword_parameters):
        time = datetime.now()

        if 'date' in keyword_parameters:
            time = keyword_parameters['date']

        ConError.last_dc = time
        ConError.total_dc += 1

        self.time = time
