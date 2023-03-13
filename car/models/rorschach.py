from abc import ABC
from car import Car
from battery.models.nubbin_battery import NubbinBattery
from engine.models.willoughby_engine import WilloughbyEngine
from datetime import date, datetime


class Rorschach(Car, ABC):
    def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int,
                 current_date: date = datetime.today().date()):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(last_service_date, current_date)
        super().__init__(self.engine, self.battery)
