from project.other.validator import Validator
from project.table.table import Table


class OutsideTable(Table):

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.num_is_between(value, 51, 100, "Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value
