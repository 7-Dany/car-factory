import unittest
from tire.models.octoprime_tire import Octoprime


class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        wear_numbers = [0.7, 0.7, 0.8, 0.8]
        tire = Octoprime(wear_numbers)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        wear_numbers = [0.7, 0.7, 0.7, 0.7]
        tire = Octoprime(wear_numbers)
        self.assertFalse(tire.needs_service())
