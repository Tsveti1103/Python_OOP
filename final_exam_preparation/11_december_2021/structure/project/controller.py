from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    cars_types = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if any(c.model == model for c in self.cars):
            raise Exception(f"Car {model} is already created!")
        if car_type in self.cars_types:
            car = self.cars_types[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.find_by_name(driver_name, self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.find_by_name(race_name, self.races):
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        obj = self.find_by_name(driver_name, self.drivers)
        if not obj:
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = obj
        cars_available = []
        for car in self.cars:
            if car.type == car_type and car.is_taken == False:
                cars_available.append(car)
        if not cars_available:
            raise Exception(f"Car {car_type} could not be found!")
        car = cars_available[-1]
        car.is_taken = True
        if driver.car is None:
            driver.car = car
            return f"Driver {driver_name} chose the car {car.model}."
        old_car = driver.car
        old_car.is_taken = False
        driver.car = car
        return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.find_by_name(race_name, self.races)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.find_by_name(driver_name, self.drivers)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.find_by_name(race_name, self.races)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        race_winners = sorted(race.drivers, key=lambda r: r.car.speed_limit, reverse=True)[:3]
        result = ''
        for driver in race_winners:
            driver.number_of_wins += 1
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"
        return result.strip()

    @staticmethod
    def find_by_name(name, list):
        if any(d.name == name for d in list):
            obj = [d for d in list if d.name == name][0]
            return obj
        return None
