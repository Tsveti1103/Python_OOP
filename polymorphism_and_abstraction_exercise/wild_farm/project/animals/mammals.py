from test.project import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ['Vegetable', 'Fruit']
    WEIGHT_INCREASE = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREASE = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOODS = ['Meat', 'Vegetable']
    WEIGHT_INCREASE = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREASE = 1.00

    def make_sound(self):
        return "ROAR!!!"
