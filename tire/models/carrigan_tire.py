from tire import Tire
from abc import ABC


class Carrigan(Tire, ABC):
    def __init__(self, wear_numbers: [float]):
        self.wear_numbers = wear_numbers

    def needs_service(self) -> bool:
        is_service_needed = False
        for i in self.wear_numbers:
            if i >= 0.9:
                is_service_needed = True
                break
        return is_service_needed
