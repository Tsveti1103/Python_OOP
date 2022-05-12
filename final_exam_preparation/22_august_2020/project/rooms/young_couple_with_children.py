from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, name, salary_one, salary_two, *children):
        super().__init__(name, salary_one + salary_two, (len(children) + 2))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = self.generate_appliances(TV, Fridge, Laptop)
        self.calculate_expenses(self.appliances, self.children)
