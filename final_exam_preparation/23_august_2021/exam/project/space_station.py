from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.other.validator import Validator
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    astronaut_types = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}
    number_of_successful_missions = 0
    number_of_not_completed_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type, name):
        if astronaut_type not in self.astronaut_types:
            raise Exception("Astronaut type is not valid!")
        astronaut = Validator.find_by_name_in_list(name, self.astronaut_repository.astronauts)
        if astronaut:
            return f"{name} is already added."
        new_astronaut = self.astronaut_types[astronaut_type](name)
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        planet = Validator.find_by_name_in_list(name, self.planet_repository.planets)
        if planet:
            return f"{name} is already added."
        new_planet = Planet(name)
        new_planet.items = items.split(', ')
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = Validator.find_by_name_in_list(name, self.astronaut_repository.astronauts)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name):
        planet = Validator.find_by_name_in_list(planet_name, self.planet_repository.planets)
        if planet is None:
            raise Exception("Invalid planet name!")
        best_astronauts = []
        for a in self.astronaut_repository.astronauts:
            if a.oxygen > 30:
                best_astronauts.append(a)
        if not best_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        best_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda a: a.oxygen, reverse=True)[:5]
        astronauts_count = 0
        for astronaut in best_astronauts:
            astronauts_count += 1
            while planet.items:
                astronaut.backpack.append(planet.items.pop(-1))
                astronaut.breathe()
                if not planet.items:
                    self.number_of_successful_missions += 1
                    return f"Planet: {planet_name} was explored. {astronauts_count} astronauts participated in collecting items."
                if astronaut.oxygen == 0:
                    break
        self.number_of_not_completed_missions += 1
        return "Mission is not completed."

    def report(self):
        result = f"{self.number_of_successful_missions} successful missions!\n{self.number_of_not_completed_missions} missions were not completed!\nAstronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}\n"
            result += f"Oxygen: {astronaut.oxygen}\n"
            if not astronaut.backpack:
                astronaut.backpack.append("none")
            result += f"Backpack items: {', '.join(astronaut.backpack)}\n"
        return result


# a = Biologist("1")
# a1 = Geodesist("2")
# a2 = Meteorologist("3")
# a3 = Meteorologist("4")
# a4 = Meteorologist("5")
# a5 = Meteorologist("6")
# a6 = Meteorologist("7")
# a7 = Meteorologist("8")
x = SpaceStation()
p = Planet("Blabla")
# x.add_astronaut("Biologist", "a0")
x.add_astronaut("Geodesist", "a1")
# x.add_astronaut("Meteorologist", "a2")
# x.add_astronaut("Meteorologist", "a3")
# x.add_astronaut("Meteorologist", "a4")
# x.add_astronaut("Meteorologist", "a5")
# x.add_astronaut("Meteorologist", "a6")
# x.add_astronaut("Meteorologist", "a7")
x.add_planet("Blabla", "ASD, WQE, GDS, ASDQA, ASDQ")
x.send_on_mission('Blabla')
print(x.report())
