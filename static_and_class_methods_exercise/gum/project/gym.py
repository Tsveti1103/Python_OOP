class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, new_equipment):
        if new_equipment not in self.equipment:
            self.equipment.append(new_equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        result = ''
        subscription = self.__find_by_id(self.subscriptions, subscription_id)
        customer = self.__find_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_by_id(self.trainers, subscription.trainer_id)
        plan = self.__find_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_by_id(self.equipment, plan.equipment_id)
        result += str(subscription) + "\n"
        result += str(customer) + "\n"
        result += str(trainer) + "\n"
        result += str(equipment) + "\n"
        result += str(plan) + "\n"
        return result

    def __find_by_id(self, collection, current_id):
        for x in collection:
            if x.id == current_id:
                return x
