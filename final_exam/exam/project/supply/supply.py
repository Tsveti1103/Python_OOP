from abc import ABC, abstractmethod

from project.validator import Validator


class Supply(ABC):
    @abstractmethod
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.type = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.empty_string(value, "Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        Validator.value_is_less_than_num(value, 0, "Energy cannot be less than zero.")
        self.__energy = value

    def details(self):
        return f"{self.type}: {self.name}, {self.energy}"
