class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def __customer_by_id(self, customer_id):
        customer = [customer for customer in self.customers if customer_id == customer.id][0]
        return customer

    def __dvd_by_id(self, dvd_id):
        dvd = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]
        return dvd

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__customer_by_id(customer_id)
        dvd = self.__dvd_by_id(dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__customer_by_id(customer_id)
        dvd = self.__dvd_by_id(dvd_id)
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for c in self.customers:
            result += str(c) + '\n'
        for d in self.dvds:
            result += str(d) + '\n'
        return result



