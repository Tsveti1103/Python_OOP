class Validator:
    @staticmethod
    def empty_string(text, message):
        if text.strip() == "":
            raise ValueError(message)
        return text

    @staticmethod
    def value_is_less_than_num(value, num, message):
        if value < num:
            raise ValueError(message)

    @staticmethod
    def value_is_between(value, min_num, max_num, message):
        if min_num > value or value > max_num:
            raise ValueError(message)

    @staticmethod
    def find_by_name(name, all_obj):
        for obj in all_obj:
            if obj.name == name:
                return obj

    @staticmethod
    def find_by_type(o_type, all_obj):
        res = []
        for obj in all_obj:
            if obj.type == o_type:
                res.append(obj)
        if not res:
            if o_type == "Food":
                raise Exception("There are no food supplies left!")
            elif o_type == "Drink":
                raise Exception("There are no drink supplies left!")
        return res[-1]
