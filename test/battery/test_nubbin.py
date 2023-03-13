import unittest
from battery.models.nubbin_battery import NubbinBattery
from datetime import datetime


class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
