class Child:
    def __init__(self, food_cost, *toys_cost):
        self.toys_cost = toys_cost
        self.food_cost = food_cost
        self.cost = sum(self.toys_cost) + self.food_cost

    def get_monthly_expense(self):
        monthly_expense = self.cost * 30
        return monthly_expense
