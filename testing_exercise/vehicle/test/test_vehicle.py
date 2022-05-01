from unittest import TestCase, main

from test.project import Vehicle


class TestVehicle(TestCase):
    def test_initialisation(self):
        car = Vehicle(50.0, 150.0)
        self.assertEqual(50.0, car.fuel)
        self.assertEqual(50.0, car.capacity)
        self.assertEqual(150.0, car.horse_power)
        self.assertEqual(1.25, car.fuel_consumption)

    def test_drive_raises_error(self):
        car = Vehicle(50.0, 150.0)
        with self.assertRaises(Exception) as ex:
            car.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_correct_data(self):
        car = Vehicle(50.0, 150.0)
        car.drive(4)
        self.assertEqual(45, car.fuel)

    def test_refuel_raises_error(self):
        car = Vehicle(50.0, 150.0)
        with self.assertRaises(Exception) as ex:
            car.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_correct_data(self):
        car = Vehicle(50.0, 150.0)
        car.drive(4)
        car.refuel(4)
        self.assertEqual(49, car.fuel)

    def test_str(self):
        car = Vehicle(50.0, 150.0)
        result = str(car)
        self.assertEqual("The vehicle has 150.0 horse power with 50.0 fuel left and 1.25 fuel consumption", result)


if __name__ == "__main__":
    main()
