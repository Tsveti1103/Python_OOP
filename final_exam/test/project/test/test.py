
from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
    def test_init(self):
        m = Movie("asd", 1887, 5.2)
        self.assertEqual("asd", m.name)
        self.assertEqual(1887, m.year)
        self.assertEqual(5.2, m.rating)
        self.assertEqual([], m.actors)

        with self.assertRaises(ValueError) as ex:
            m = Movie("", 1887, 5.2)
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            m = Movie("asd", 1886, 5.2)
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor(self):
        m = Movie("asd", 1887, 5.2)
        m.add_actor("Pesho")
        self.assertEqual(['Pesho'], m.actors)
        result = m.add_actor("Pesho")
        self.assertEqual("Pesho is already added in the list of actors!", result)

    def test_gt(self):
        m = Movie("asd1", 1887, 6)
        m2 = Movie("asd", 1887, 5)
        result = m > m2
        self.assertEqual('"asd1" is better than "asd"', result)

        m = Movie("asd1", 1887, 6)
        m2 = Movie("asd", 1887, 7)
        result = m > m2
        self.assertEqual('"asd" is better than "asd1"', result)

        m = Movie("asd1", 1887, 6)
        m2 = Movie("asd", 1887, 7)
        result = m < m2
        self.assertEqual('"asd" is better than "asd1"', result)

        m = Movie("asd1", 1887, 6)
        m2 = Movie("asd", 1887, 5)
        result = m < m2
        self.assertEqual('"asd1" is better than "asd"', result)

    def test_repr(self):
        m = Movie("asd", 1900, 5.2)
        m.add_actor("Pesho")
        m.add_actor("Pesho2")
        result = m.__repr__()
        self.assertEqual(f"Name: asd\n"
                         f"Year of Release: 1900\n"
                         f"Rating: 5.20\n"
                         f"Cast: Pesho, Pesho2",result)


if __name__ == '__main__':
    main()
