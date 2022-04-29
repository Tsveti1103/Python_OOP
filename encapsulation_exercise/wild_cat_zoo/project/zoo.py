from test.project import Animal
from test.project import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary
        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_tend = 0
        for animal in self.animals:
            total_tend += animal.money_for_care
        if total_tend <= self.__budget:
            self.__budget -= total_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__entity_str(self.animals, "Lion")
        result += self.__entity_str(self.animals, "Tiger")
        result += self.__entity_str(self.animals, "Cheetah")
        return result.strip()

    def __entity_str(self, entities, entity_type):
        counter = 0
        result = ""
        for animal in entities:
            if animal.__class__.__name__ == entity_type:
                counter += 1
                result += repr(animal) + "\n"
        return f"----- {counter} {entity_type}s:\n" + result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__entity_str(self.workers, "Keeper")
        result += self.__entity_str(self.workers, "Caretaker")
        result += self.__entity_str(self.workers, "Vet")
        return result.strip()
