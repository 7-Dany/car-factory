from battery import Battery
from abc import ABC
from datetime import timedelta, date


class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date: date, current_date: date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        time_since_last_service = self.current_date - self.last_service_date
        if time_since_last_service >= timedelta(days=365 * 2):
            return True
        else:
            return False
