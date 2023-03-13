from tire import Tire
from abc import ABC


class Octoprime(Tire, ABC):
    def __init__(self, wear_numbers: [float]):
        self.wear_numbers = wear_numbers

    def needs_service(self) -> bool:
        sum_wear = sum(self.wear_numbers)
        return sum_wear >= 3
