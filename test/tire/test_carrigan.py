import unittest
from tire.models.carrigan_tire import Carrigan


class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        wear_sensor_results = [0.8, 0.7, 0.9, 1]
        tire = Carrigan(wear_sensor_results)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        wear_sensor_results = [0.8, 0.7, 0.8, 0.8]
        tire = Carrigan(wear_sensor_results)
        self.assertFalse(tire.needs_service())
