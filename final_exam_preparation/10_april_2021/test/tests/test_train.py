from unittest import TestCase, main

from project.train.train import Train


class Test(TestCase):

    def test_init(self):
        train1 = Train('Tutu', 20)
        self.assertEqual('Tutu', train1.name)
        self.assertEqual(20, train1.capacity)
        self.assertEqual("Train is full", train1.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", train1.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", train1.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", train1.PASSENGER_ADD)
        self.assertEqual("Removed {}", train1.PASSENGER_REMOVED)
        self.assertEqual(0, train1.ZERO_CAPACITY)
        self.assertEqual([], train1.passengers)

    def test_add_full_train(self):
        train1 = Train('Tutu', 0)

        with self.assertRaises(ValueError) as ex:
            train1.add('Ivan')
        self.assertEqual("Train is full", str(ex.exception))

    def test_add(self):
        train2 = Train('Tutu', 20)
        res = train2.add('Ivan')
        self.assertEqual("Added passenger Ivan", res)
        with self.assertRaises(ValueError) as ex:
            train2.add('Ivan')
        self.assertEqual("Passenger Ivan Exists", str(ex.exception))

    def test_remove(self):
        train1 = Train('Tutu', 20)
        with self.assertRaises(ValueError) as ex:
            train1.remove('Ivan')
        self.assertEqual("Passenger Not Found", str(ex.exception))
        train1.add('Ivan')
        res = train1.remove('Ivan')
        self.assertEqual("Removed Ivan", res)


if __name__ == '__main__':
    main()
