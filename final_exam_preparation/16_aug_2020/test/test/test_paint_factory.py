from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPlantFactory(TestCase):
    def setUp(self):
        self.fac = PaintFactory("MyFac", 6)

    def test_init(self):
        self.assertEqual(6, self.fac.capacity)
        self.assertEqual({}, self.fac.ingredients)

    def test_add_ingredient(self):
        self.fac.add_ingredient("white", 1)
        self.fac.add_ingredient("yellow", 1)
        self.fac.add_ingredient("blue", 1)
        self.fac.add_ingredient("green", 1)
        self.fac.add_ingredient("red", 1)
        self.assertEqual({"white": 1, "yellow": 1, "blue": 1, "green": 1, "red": 1}, self.fac.ingredients)

        with self.assertRaises(ValueError) as ex:
            self.fac.add_ingredient("yellow", 5)
        self.assertEqual("Not enough space in factory", str(ex.exception))

        with self.assertRaises(TypeError) as ex:
            self.fac.add_ingredient("dark_red", 1)
        self.assertEqual("Ingredient of type dark_red not allowed in PaintFactory", str(ex.exception))

    def test_remove_ingredient(self):
        self.fac.add_ingredient("white", 1)
        self.fac.add_ingredient("yellow", 1)
        self.fac.add_ingredient("white", 1)
        self.assertEqual({"white": 2, "yellow": 1}, self.fac.ingredients)
        self.assertEqual({"white": 2, "yellow": 1}, self.fac.products)

        with self.assertRaises(KeyError) as ex:
            self.fac.remove_ingredient("blue", 5)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.fac.remove_ingredient('white', 3)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

        self.fac.remove_ingredient('white', 2)
        self.assertEqual({"white": 0, "yellow": 1}, self.fac.ingredients)

    def test_repr(self):
        self.fac.add_ingredient("white", 1)
        self.fac.add_ingredient("yellow", 1)
        self.fac.add_ingredient("white", 1)
        excepted = "Factory name: MyFac with capacity 6.\nwhite: 2\nyellow: 1\n"
        real = str(self.fac)
        self.assertEqual(excepted, real)


if __name__ == '__main__':
    main()
