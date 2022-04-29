from test.project import Dough
from test.project import Topping


class Pizza:
    def __init__(self, name, dough: Dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        else:
            self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        else:
            self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        else:
            self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        if self.toppings_capacity == len(self.toppings):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight

        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        dough_weight = self.dough.weight
        topping_weight = 0
        for top, w in self.toppings.items():
            topping_weight += w

        return dough_weight + topping_weight
