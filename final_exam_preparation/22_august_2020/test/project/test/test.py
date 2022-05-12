from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):

    def test_init(self):
        student = StudentReportCard("Pesho", 12)
        self.assertEqual("Pesho", student.student_name)
        self.assertEqual(12, student.school_year)
        self.assertEqual({}, student.grades_by_subject)

        student = StudentReportCard("Pesho", 1)
        self.assertEqual(1, student.school_year)

    def test_name_errors(self):
        with self.assertRaises(ValueError) as ex:
            student = StudentReportCard("", 10)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            student = StudentReportCard("", 0)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_school_year_errors(self):
        with self.assertRaises(ValueError) as ex:
            student = StudentReportCard("Pesho", 0)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            student = StudentReportCard("Pesho", 13)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_add_grade(self):
        student = StudentReportCard("Pesho", 10)
        student.add_grade('Chemistry', 5.5)
        self.assertEqual({'Chemistry': [5.5]}, student.grades_by_subject)

        student.add_grade('Math', 4.5)
        self.assertEqual({'Chemistry': [5.5], 'Math': [4.5]}, student.grades_by_subject)

        student.add_grade('Chemistry', 4.5)
        self.assertEqual({'Chemistry': [5.5, 4.5], 'Math': [4.5]}, student.grades_by_subject)

    def test_average_grade_by_subject(self):
        student = StudentReportCard("Pesho", 10)
        self.assertEqual('', student.average_grade_by_subject())

        student.add_grade('Chemistry', 3.5)
        result = student.average_grade_by_subject()
        expected = 'Chemistry: 3.50'
        self.assertEqual(expected, result)

        student.add_grade('Chemistry', 4.5)
        result = student.average_grade_by_subject()
        expected = 'Chemistry: 4.00'
        self.assertEqual(expected, result)

        student.add_grade('Math', 4.5)
        student.add_grade('Math', 5.5)
        result = student.average_grade_by_subject()
        expected = f'Chemistry: 4.00\nMath: 5.00'
        self.assertEqual(expected, result)

    def test_average_grade_for_all_subjects(self):
        student = StudentReportCard("Pesho", 10)
        student.add_grade('Chemistry', 0)
        result = student.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 0.00", result)

        student.add_grade('Chemistry', 4.0)
        result = student.average_grade_for_all_subjects()
        expected = f'Average Grade: 2.00'
        self.assertEqual(expected, result)

        student.add_grade('Chemistry', 4.0)
        student.add_grade('Math', 4.5)
        student.add_grade('Math', 2.5)
        result = student.average_grade_for_all_subjects()
        expected = f'Average Grade: 3.00'
        self.assertEqual(expected, result)

    def test_repr(self):
        student = StudentReportCard("Pesho", 10)
        student.add_grade('Chemistry', 3.5)
        result = student.__repr__()
        expected = f'Name: Pesho\nYear: 10\n----------\nChemistry: 3.50\n----------\nAverage Grade: 3.50'
        self.assertEqual(expected, result)

        student.add_grade('Chemistry', 4.5)
        student.add_grade('Math', 4.5)
        student.add_grade('Math', 5.5)
        result = student.__repr__()
        expected = f'Name: Pesho\nYear: 10\n----------\nChemistry: 4.00\nMath: 5.00\n----------\nAverage Grade: 4.50'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
