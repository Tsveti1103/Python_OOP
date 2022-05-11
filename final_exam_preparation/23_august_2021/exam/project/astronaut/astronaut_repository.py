
from project.other.validator import Validator


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        astronaut = Validator.find_by_name_in_list(name, self.astronauts)
        return astronaut
