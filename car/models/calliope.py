from abc import ABC
from car import Car
from engine.models.capulet_engine import CapuletEngine
from battery.models.spindler_battery import SpindlerBattery
from datetime import date, datetime


class Calliope(Car, ABC):

    def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int,
                 current_date: date = datetime.today().date()):
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        super().__init__(self.engine, self.battery)
