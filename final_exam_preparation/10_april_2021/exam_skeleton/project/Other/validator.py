class Validator:
    @staticmethod
    def empty_string(value, message):
        if value == "":
            raise ValueError(message)

    @staticmethod
    def is_positive_number(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def find_by_name(name, all_obj):
        for obj in all_obj:
            if obj.name == name:
                return obj





