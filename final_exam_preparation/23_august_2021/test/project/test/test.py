from test.project import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def test_initialisation(self):
        l = Library('Lib')
        self.assertEqual({}, l.books_by_authors)
        self.assertEqual('Lib', l.name)
        self.assertEqual({}, l.readers)
        with self.assertRaises(ValueError) as ex:
            l = Library('')
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book(self):
        l = Library('Lib')
        l.add_book('John', 'Python')
        self.assertEqual({'John': ['Python']}, l.books_by_authors)
        l.add_book('John', 'Python')
        self.assertEqual({'John': ['Python']}, l.books_by_authors)
        l.add_book('John', 'Python2')
        self.assertEqual({'John': ['Python', 'Python2']}, l.books_by_authors)

    def test_add_rider(self):
        l = Library('Lib')
        self.assertEqual({}, l.readers)
        l.add_reader('Pesho')
        self.assertEqual({"Pesho": []}, l.readers)
        self.assertEqual(f"Pesho is already registered in the {l.name} library.", l.add_reader('Pesho'))

    def test_rent_book_invalid_reader_name(self):
        l = Library('Lib')
        self.assertEqual("Pesho is not registered in the Lib Library.", l.rent_book('Pesho', 'John', 'Python'))
        l.add_reader('Pesho')
        self.assertEqual("Lib Library does not have any John's books.", l.rent_book('Pesho', 'John', 'Python'))
        l.add_book('John', 'Python2')
        self.assertEqual("Lib Library does not have John's \"Python\".", l.rent_book('Pesho', 'John', 'Python'))
        l.rent_book('Pesho', "John", "Python2")
        self.assertEqual([{'John': 'Python2'}], l.readers['Pesho'])
        self.assertEqual({'John': []}, l.books_by_authors)


if __name__ == "__main__":
    main()
