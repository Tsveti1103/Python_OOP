from unittest import TestCase, main

from test.project import Student


class TestStudent(TestCase):
    def test_initialisation(self):
        student = Student('Pesho')
        self.assertEqual('Pesho', student.name)
        self.assertEqual({}, student.courses)

        student = Student('Pesho', {'asd': [1, 2, 3]})
        self.assertEqual('Pesho', student.name)
        self.assertEqual({'asd': [1, 2, 3]}, student.courses)

        student = Student('Pesho', None)
        self.assertEqual('Pesho', student.name)
        self.assertEqual({}, student.courses)

    def test_add_notes_correct_data(self):
        student = Student('Pesho', {"course1": []})
        result = student.add_notes("course1", "first")
        self.assertEqual({"course1": ["first"]}, student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_raise_error(self):
        student = Student('Pesho')
        with self.assertRaises(Exception) as ex:
            student.add_notes("course1", "first")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({}, student.courses)

    def test_leave_course_correct_data(self):
        student = Student('Pesho', {"course1": [1, 2, 3], "course2": [4, 5, 6]})
        result = student.leave_course("course1")
        self.assertEqual({"course2": [4, 5, 6]}, student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_raise_error(self):
        student = Student('Pesho')
        with self.assertRaises(Exception) as ex:
            student.leave_course("course1")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual({}, student.courses)

    def test_enroll_if_course_in_courses_and_update_notes(self):
        student = Student('Pesho', {"course1": [1, 2, 3], "course2": [4, 5, 6]})
        result = student.enroll('course1', [4])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"course1": [1, 2, 3, 4], "course2": [4, 5, 6]}, student.courses)

        result = student.enroll('course1', [5], 'Y')
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"course1": [1, 2, 3, 4, 5], "course2": [4, 5, 6]}, student.courses)

    def test_enroll_if_course_not_in_courses_and_add_course_and_notes(self):
        student = Student('Pesho', {"course1": [1, 2, 3], "course2": [4, 5, 6]})
        result = student.enroll('course3', [4])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"course1": [1, 2, 3], "course2": [4, 5, 6], "course3": [4]}, student.courses)
        student = Student('Pesho', {"course1": [1, 2, 3], "course2": [4, 5, 6]})
        result = student.enroll('course3', [4], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"course1": [1, 2, 3], "course2": [4, 5, 6], "course3": [4]}, student.courses)

    def test_enroll_add_only_course(self):
        student = Student('Pesho', {"course1": [1, 2, 3], "course2": [4, 5, 6]})
        result = student.enroll('course3', [4], 'N')
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"course1": [1, 2, 3], "course2": [4, 5, 6], "course3": []}, student.courses)


if __name__ == '__main__':
    main()
