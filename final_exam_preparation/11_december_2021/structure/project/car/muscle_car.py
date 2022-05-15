from project.car.car import Car


class MuscleCar(Car):
    min_speed_limit = 250
    max_speed_limit = 450
    type = "MuscleCar"

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)
