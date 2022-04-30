class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class TestIntegerList(TestCase):

    def test_initialization(self):
        current_obj = IntegerList()
        self.assertEqual([], current_obj._IntegerList__data)
        current_obj = IntegerList(5, '4', 4.2)
        self.assertEqual([5], current_obj._IntegerList__data)

    def test_add_element_correct_data(self):
        current_obj = IntegerList(5)
        self.assertEqual([5], current_obj.get_data())  # self.assertEqual([5], current_obj._IntegerList__data)
        current_obj.add(7)
        self.assertEqual([5, 7], current_obj.get_data())

    def test_add_element_incorrect_data(self):
        current_obj = IntegerList(5)
        self.assertEqual([5], current_obj._IntegerList__data)
        with self.assertRaises(ValueError) as ex:
            current_obj.add('asd')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_correct_data(self):
        current_obj = IntegerList(5, 7, 8)
        result = current_obj.remove_index(0)
        self.assertEqual([7, 8], current_obj._IntegerList__data)
        self.assertEqual(5, result)
        result = current_obj.remove_index(1)
        self.assertEqual([7], current_obj._IntegerList__data)
        self.assertEqual(8, result)

    def test_remove_index_raises(self):
        current_obj = IntegerList(5, 7, 8)
        with self.assertRaises(IndexError) as ex:
            current_obj.remove_index(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_correct_data(self):
        current_obj = IntegerList(5, 7, 8)
        result = current_obj.get(0)
        self.assertEqual(5, result)

    def test_get_raises(self):
        current_obj = IntegerList(5, 7, 8)
        with self.assertRaises(IndexError) as ex:
            current_obj.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_correct_data(self):
        current_obj = IntegerList(5)
        current_obj.insert(0, 4)
        self.assertEqual([4, 5], current_obj._IntegerList__data)

    def test_insert_index_error(self):
        current_obj = IntegerList(5)
        with self.assertRaises(IndexError) as ex:
            current_obj.insert(5, 4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_value_error(self):
        current_obj = IntegerList(5)
        with self.assertRaises(ValueError) as ex:
            current_obj.insert(0, "4")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest(self):
        current_obj = IntegerList(5, 7, 8)
        result = current_obj.get_biggest()
        self.assertEqual(8, result)

    def test_get_index(self):
        current_obj = IntegerList(5, 7, 8)
        result = current_obj.get_index(5)
        self.assertEqual(0, result)
        result = current_obj.get_index(8)
        self.assertEqual(2, result)


if __name__ == "__main__":
    main()
