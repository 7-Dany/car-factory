from datetime import datetime
import unittest
from battery.models.spindler_battery import SpindlerBattery


class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
