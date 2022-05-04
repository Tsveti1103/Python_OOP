from test.project import Bird


class Owl(Bird):

    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREASE = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):

    ALLOWED_FOODS = ['Meat', 'Vegetable', 'Fruit', 'Seed']
    WEIGHT_INCREASE = 0.35

    def make_sound(self):
        return "Cluck"
