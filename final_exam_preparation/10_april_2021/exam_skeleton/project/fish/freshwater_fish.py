from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    size_increase = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)
        self.aquarium_type = "FreshwaterAquarium"