from test.project import Food


class MainDish(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)
