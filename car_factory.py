from car.models.thovex import Thovex
from car.models.rorschach import Rorschach
from car.models.glissade import Glissade
from car.models.palindrome import Palindrome
from car.models.calliope import Calliope
from datetime import date


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int, wear_numbers: [float]) -> Calliope:
        return Calliope(last_service_date, current_mileage, last_service_mileage, wear_numbers, current_date)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int, wear_numbers: [float]) -> Glissade:
        return Glissade(last_service_date, current_mileage, last_service_mileage, wear_numbers, current_date)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_is_on: bool,
                          wear_numbers: [float]) -> Palindrome:
        return Palindrome(last_service_date, warning_light_is_on, wear_numbers, current_date)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int,
                         last_service_mileage: int, wear_numbers: [float]) -> Rorschach:
        return Rorschach(last_service_date, current_mileage, last_service_mileage, wear_numbers, current_date)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int,
                      last_service_mileage: int, wear_numbers: [float]) -> Thovex:
        return Thovex(last_service_date, current_mileage, last_service_mileage, wear_numbers, current_date)
