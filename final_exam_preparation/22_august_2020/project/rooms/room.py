class Room:
    room_cost = 0
    appliances = []

    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for el in args:
            result += sum(o.get_monthly_expense() for o in el)
        self.expenses = result

    def generate_appliances(self, *appliances_types):
        appliances = []
        for _ in range(self.members_count):
            for appliance in appliances_types:
                appliances.append(appliance())
        return appliances

    @property
    def total_expenses(self):
        return self.expenses + self.room_cost
