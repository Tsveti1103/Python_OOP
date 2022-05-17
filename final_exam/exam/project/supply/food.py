from project.supply.supply import Supply


class Food(Supply):
    def __init__(self, name, energy=25):
        super().__init__(name, energy)
        self.type = "Food"
