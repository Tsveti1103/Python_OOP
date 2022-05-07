from zoo.project import Employee
from zoo.project import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
