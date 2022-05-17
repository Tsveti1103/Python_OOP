from project.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name):
        super().__init__(name, 15)
        self.type = "Drink"
