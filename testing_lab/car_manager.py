class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


car = Car("a", "b", 1, 4)
car.make = ""
print(car)

from unittest import TestCase, main


class TestCar(TestCase):
    def test_initialisation(self):
        car = Car('Bg', "Opel", 12, 50)
        self.assertEqual("Bg", car.make)
        self.assertEqual("Opel", car.model)
        self.assertEqual(12, car.fuel_consumption)
        self.assertEqual(50, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_make_raise_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car('', "Opel", 12, 50)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_raise_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Bg', "", 12, 50)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_raise_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Bg', "Opel", 0, 50)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_raise_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Bg', "Opel", 12, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_raise_error(self):
        car = Car('Bg', "Opel", 12, 50)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_raise_error(self):
        car = Car('Bg', "Opel", 12, 50)
        with self.assertRaises(Exception) as ex:
            car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_correct_data(self):
        car = Car('Bg', "Opel", 12, 50)
        car.refuel(20)
        self.assertEqual(20, car.fuel_amount)
        car.refuel(60)
        self.assertEqual(50, car.fuel_amount)

    def test_drive_raise_error(self):
        car = Car('Bg', "Opel", 12, 50)
        with self.assertRaises(Exception) as ex:
            car.drive(5)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_correct_data(self):
        car = Car('Bg', "Opel", 10, 50)
        car.refuel(50)
        car.drive(200)
        self.assertEqual(30, car.fuel_amount)


if __name__ == '__main__':
    main()
