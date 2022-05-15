from project.car.car import Car


class SportsCar(Car):
    min_speed_limit = 400
    max_speed_limit = 600
    type = "SportsCar"

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)
