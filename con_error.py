from datetime import datetime


class con_error:

    total_dc = 0
    last_dc = "Never"

    def __init__(self):
        con_error.last_dc = datetime.now()
        con_error.total_dc += 1
