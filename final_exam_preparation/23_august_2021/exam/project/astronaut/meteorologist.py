from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    oxygen_decreasing = 15

    def __init__(self, name):
        super().__init__(name, 90)