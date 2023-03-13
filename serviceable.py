from car import Car


class Serviceable:
    def __init__(self, car: Car):
        self.car = car

    def needs_service(self) -> bool:
        return self.car.needs_service()
