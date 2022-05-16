from abc import ABC, abstractmethod

from project.Other.validator import Validator


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.empty_string(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        total_comfort = 0
        for decor in self.decorations:
            total_comfort += decor.comfort
        return total_comfort

    def add_fish(self, fish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."
        fish_type = fish.__class__.__name__
        self.fish.append(fish)
        return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_names = [fish.name for fish in self.fish]
        if not fish_names:
            fish_names.append("none")
        return f"{self.name}:\nFish: {' '.join(fish_names)}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"
