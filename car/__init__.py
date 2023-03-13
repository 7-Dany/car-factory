from abc import ABC


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        if self.battery.needs_service() or self.engine.needs_service():
            return True
        else:
            return False
