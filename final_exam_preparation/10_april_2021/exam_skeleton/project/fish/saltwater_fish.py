from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    size_increase = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)
        self.aquarium_type = "SaltwaterAquarium"
