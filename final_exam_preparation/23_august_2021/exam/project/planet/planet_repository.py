from project.other.validator import Validator


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet):
        self.planets.append(planet)

    def remove(self, planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        planet = Validator.find_by_name_in_list(name, self.planets)
        return planet

