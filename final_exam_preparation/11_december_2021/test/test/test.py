from test.project import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def test_initialisation(self):
        t = Team('First')
        self.assertEqual("First", t.name)
        self.assertEqual({}, t.members)
        with self.assertRaises(ValueError) as ex:
            t = Team('First5')
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member(self):
        t = Team('First')
        result = t.add_member(One=20, Two=25, Three=30)
        self.assertEqual('Successfully added: One, Two, Three', result)

        t = Team('First')
        t.add_member(One=20, Two=25, Three=30)
        result = t.add_member(One=20)
        self.assertEqual('Successfully added: ', result)

    def test_remove_member(self):
        t = Team('First')
        t.add_member(One=20, Two=25, Three=30)
        result = t.remove_member('One')
        self.assertEqual("Member One removed", result)
        self.assertEqual({'Two': 25, 'Three': 30}, t.members)
        result = t.remove_member('One')
        self.assertEqual('Member with name One does not exist', result)

    def test_gt_function_true(self):
        t = Team('First')
        t2 = Team('Second')
        t.add_member(One=20, Two=25, Three=30)
        t2.add_member(One=20, Two=25)
        result = t.__gt__(t2)
        self.assertEqual(True, result)
        result = t > t2
        self.assertEqual(True, result)

    def test_gt_function_false(self):
        t = Team('First')
        t2 = Team('Second')
        t2.add_member(One=20, Two=25, Three=30)
        t.add_member(One=20, Two=25)
        result = t > t2
        self.assertEqual(False, result)
        result = t.__gt__(t2)
        self.assertEqual(False, result)

    def test_len(self):
        t = Team('First')
        t.add_member(One=20, Two=25, Three=30)
        result = len(t)
        self.assertEqual(3, result)

    def test_add(self):
        t = Team('First')
        t2 = Team('Second')
        t2.add_member(One=20, Two=25, Three=30)
        t.add_member(Four=20, Five=25)
        t3 = t + t2
        self.assertEqual('FirstSecond', t3.name)
        result = t3.members
        self.assertEqual({'Four': 20, 'Five': 25, 'One': 20, 'Two': 25, 'Three': 30}, result)

    def test_str_method(self):
        t = Team('First')
        t.add_member(b=20, a=25, f=18)
        result = str(t)
        expected = f'Team name: First\nMember: a - 25-years old\nMember: b - 20-years old\nMember: f - 18-years old'
        self.assertEqual(expected, result)
        t = Team('First')
        result = str(t)
        expected = f'Team name: First'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
