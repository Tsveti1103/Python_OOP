class Cat:

    def __init__(self, name):
        # TODO
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def test_cat_size_increased_after_eating(self):
        cat = Cat('cat')
        self.assertEqual(0, cat.size)
        cat.eat()
        self.assertEqual(1, cat.size)

    def test_cat_fed_after_eating(self):
        cat = Cat('cat')
        self.assertFalse(cat.fed)
        cat.eat()
        self.assertTrue(cat.fed)

    def test_if_fed_cannot_eat(self):
        cat = Cat('cat')
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_fall_asleep_if_not_fed_raises(self):
        cat = Cat('cat')
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_not_sleepy_after_sleeping(self):
        cat = Cat('cat')
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    main()
