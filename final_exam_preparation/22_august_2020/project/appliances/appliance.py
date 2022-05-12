class Appliance:
    def __init__(self, cost):
        self.cost = cost

    def get_monthly_expense(self):
        monthly_expense = self.cost * 30
        return monthly_expense
