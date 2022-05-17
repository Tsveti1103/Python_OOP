from project.validator import Validator


class Player:
    names = []

    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self._need_sustenance = None

    @property
    def name(self):

        return self.__name

    @name.setter
    def name(self, value):
        Validator.empty_string(value, "Name not valid!")
        if value in Player.names:
            raise Exception(f"Name {value} is already used!")
        self.names.append(value)

        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.value_is_less_than_num(value, 12, "The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.value_is_between(value, 0, 100, "Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        if self.stamina == 100:
            need_sustenance = False
        else:
            need_sustenance = True
        return f"Player: {self.name}, {self.age}, {self.stamina}, {need_sustenance}"
