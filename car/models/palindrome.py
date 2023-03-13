from engine.models.sternman_engine import SternmanEngine
from battery.models.spindler_battery import SpindlerBattery
from tire.models.carrigan_tire import Carrigan
from car import Car
from abc import ABC
from datetime import date, datetime


class Palindrome(Car, ABC):
    def __init__(self, last_service_date: date, warning_light_is_on: bool,
                 wear_numbers: [float], current_date: date = datetime.today().date()):
        self.engine = SternmanEngine(warning_light_is_on)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.tire = Carrigan(wear_numbers)
        super().__init__(self.engine, self.battery, self.tire)
