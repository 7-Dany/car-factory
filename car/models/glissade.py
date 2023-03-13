from abc import ABC
from car import Car
from engine.models.willoughby_engine import WilloughbyEngine
from battery.models.spindler_battery import SpindlerBattery
from tire.models.carrigan_tire import Carrigan
from datetime import date, datetime


class Glissade(Car, ABC):
    def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int,
                 wear_numbers: [float], current_date: date = datetime.today().date()):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.tire = Carrigan(wear_numbers)
        super().__init__(self.engine, self.battery, self.tire)
