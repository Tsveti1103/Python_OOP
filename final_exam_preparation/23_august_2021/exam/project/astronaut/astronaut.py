from abc import ABC, abstractmethod

from project.other.validator import Validator


class Astronaut(ABC):
    oxygen_decreasing = 10

    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_value_is_empty(value, "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.oxygen_decreasing

    def increase_oxygen(self, amount):
        self.oxygen += amount
