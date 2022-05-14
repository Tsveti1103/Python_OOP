class Validator:

    @staticmethod
    def value_is_not_empty_string(text, message):
        if text.strip() == "":
            raise ValueError(message)
        return text

    @staticmethod
    def value_is_positive(num, message):
        if num <= 0:
            raise ValueError(message)

    @staticmethod
    def num_is_between(num, min, max, message):
        if min > num or num > max:
            raise ValueError(message)

    @staticmethod
    def find_by_name(name, all_obj):
        for obj in all_obj:
            if obj.name == name:
                return obj

    @staticmethod
    def find_by_number(num, all_obj):
        for obj in all_obj:
            if obj.table_number == num:
                return obj
