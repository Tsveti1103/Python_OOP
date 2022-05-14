from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.other.validator import Validator
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    food_types = {"Bread": Bread, "Cake": Cake}
    drink_types = {"Tea": Tea, "Water": Water}
    table_types = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.value_is_not_empty_string(value, "Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        food = Validator.find_by_name(name, self.food_menu)
        if food:
            raise Exception(f"{food_type} {name} is already in the menu!")
        self.food_menu.append(self.food_types[food_type](name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        drink = Validator.find_by_name(name, self.drinks_menu)
        if drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        self.drinks_menu.append(self.drink_types[drink_type](name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = Validator.find_by_number(table_number, self.tables_repository)
        if table:
            raise Exception(f"Table {table_number} is already in the bakery!")
        self.tables_repository.append(self.table_types[table_type](table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table = Validator.find_by_number(table_number, self.tables_repository)
        if not table:
            return f"Could not find table {table_number}"
        not_in_menu = []
        for food in args:
            current_food = Validator.find_by_name(food, self.food_menu)
            if current_food:
                table.order_food(current_food)
            else:
                not_in_menu.append(food)
        result = f"Table {table_number} ordered:\n"
        for food in table.food_orders:
            result += f"{food.__repr__()}\n"
        result += f"{self.name} does not have in the menu:\n"
        result += '\n'.join(not_in_menu)
        return result.strip()

    def order_drink(self, table_number: int, *args):
        table = Validator.find_by_number(table_number, self.tables_repository)
        if not table:
            return f"Could not find table {table_number}"
        not_in_menu = []
        for drink in args:
            current_drink = Validator.find_by_name(drink, self.drinks_menu)
            if current_drink:
                table.order_drink(current_drink)
            else:
                not_in_menu.append(drink)
        result = f"Table {table_number} ordered:\n"
        for drink in table.drink_orders:
            result += f"{drink.__repr__()}\n"
        result += f"{self.name} does not have in the menu:\n"
        result += '\n'.join(not_in_menu)
        return result.strip()

    def leave_table(self, table_number: int):
        table = Validator.find_by_number(table_number, self.tables_repository)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            if table.free_table_info():
                result += f"{table.free_table_info()}\n"
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"


# b = Bakery("ABC")
# print(b.add_table("InsideTable", 1, 10))
# print(b.add_table("OutsideTable", 51, 5))
# print(b.get_free_tables_info())
# print(b.add_food("Bread", "bql", 2))
# print(b.add_food("Cake", "chocolate", 5))
# b.add_drink("Tea", "black", 200, "nestea")
# print(b.add_drink("Water", "mineral", 500, "devin"))
# print(b.reserve_table(12))
# print(b.reserve_table(5))
# print(b.reserve_table(10))
# print(b.order_food(1, "asd", "keefs", "bql", "chocolate"))
# print(b.order_drink(1, "bql", "chocolate", "mineral", "black"))
