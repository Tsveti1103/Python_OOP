from project.Other.validator import Validator
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    aquarium_types = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
    decorations_types = {"Ornament": Ornament, "Plant": Plant}
    fish_types = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.aquarium_types:
            return "Invalid aquarium type."
        aquarium = self.aquarium_types[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.decorations_types:
            return "Invalid decoration type."
        decoration = self.decorations_types[decoration_type]()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = Validator.find_by_name(aquarium_name, self.aquariums)
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."
        if decoration != "None" and aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.fish_types:
            return f"There isn't a fish of type {fish_type}."
        fish = self.fish_types[fish_type](fish_name, fish_species, price)
        aquarium = Validator.find_by_name(aquarium_name, self.aquariums)
        if aquarium.capacity == len(aquarium.fish):
            return "Not enough capacity."
        aquarium_type = aquarium.__class__.__name__
        if fish.aquarium_type != aquarium_type:
            return "Water not suitable."
        aquarium.fish.append(fish)
        return f"Successfully added {fish_type} to {aquarium.name}."

    def feed_fish(self, aquarium_name: str):
        aquarium = Validator.find_by_name(aquarium_name, self.aquariums)
        aquarium.feed()
        fed_count = len(aquarium.fish)
        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        total_value = 0
        aquarium = Validator.find_by_name(aquarium_name, self.aquariums)
        fish_price = sum([fish.price for fish in aquarium.fish])
        decorations_price = sum([decor.price for decor in aquarium.decorations])
        total_value = fish_price + decorations_price
        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        result = ''
        for aq in self.aquariums:
            result += f"{str(aq)}\n"
        return result


c = Controller()
print(c.add_aquarium("FreshwaterAquarium", "1"))
print(c.add_aquarium("FreshwaterAquarium", "2"))
print(c.add_aquarium("FreshwaterAquarium", "3"))
# print(c.add_decoration("Ornament"))
# print(c.add_decoration("Plant"))
# print(c.add_decoration("Plant"))
# print(c.add_decoration("Plant"))
print(c.insert_decoration("1", "Ornament"))
print(c.insert_decoration("1", "Plant"))
print(c.insert_decoration("3", "Plant"))
print(c.insert_decoration("3", "Plant"))
print(c.add_fish("1", "FreshwaterFish", "nemo", "bla", 20))
print(c.add_fish("1", "FreshwaterFish", "nemo2", "bla", 30))
print(c.feed_fish("1"))
print(c.calculate_value("1"))
print(c.report())
