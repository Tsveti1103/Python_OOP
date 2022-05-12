class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.total_expenses
        return f"Monthly consumption: {result:.2f}$."

    def pay(self):
        res = ''
        for room in self.rooms:
            have_to_pay = room.total_expenses
            if room.budget >= have_to_pay:
                room.budget -= have_to_pay
                res += f"{room.family_name} paid {have_to_pay:.2f}$ and have {room.budget:.2f}$ left.\n"
            else:
                self.rooms.remove(room)
                res += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
        return res.strip()

    def status(self):
        all_people_in_the_hotel = sum(room.members_count for room in self.rooms)
        res = f"Total population: {all_people_in_the_hotel}\n"
        for room in self.rooms:
            res += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.members_count > 2:
                for i, v in enumerate(room.children):
                    child_cost = v.get_monthly_expense()
                    res += f"--- Child {i + 1} monthly cost: {child_cost:.2f}$\n"
            appliances_cost = sum(x.get_monthly_expense() for x in room.appliances)
            res += f"--- Appliances monthly cost: {appliances_cost:.2f}$\n"
        return res.strip()
