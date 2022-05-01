from unittest import TestCase, main

from test.project import Mammal


class TestMammal(TestCase):

    def test_initialization(self):
        animal = Mammal('Ruby', 'Dog', 'Waf')
        self.assertEqual('Ruby', animal.name)
        self.assertEqual('Dog', animal.type)
        self.assertEqual('Waf', animal.sound)
        self.assertEqual('animals', animal._Mammal__kingdom)

    def test_make_sound(self):
        animal = Mammal('Ruby', 'Dog', 'Waf')
        result = animal.make_sound()
        self.assertEqual("Ruby makes Waf", result)

    def test_get_kingdom(self):
        animal = Mammal('Ruby', 'Dog', 'Waf')
        result = animal.get_kingdom()
        self.assertEqual('animals', result)

    def test_info(self):
        animal = Mammal('Ruby', 'Dog', 'Waf')
        result = animal.info()
        self.assertEqual('Ruby is of type Dog', result)


if __name__ == "__main__":
    main()
