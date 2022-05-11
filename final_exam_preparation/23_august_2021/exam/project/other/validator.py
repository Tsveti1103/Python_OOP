class Validator:
    @staticmethod
    def check_if_value_is_empty(text, message):
        if text.strip() == "":
            raise ValueError(message)
        return text

    @staticmethod
    def find_by_name_in_list(name, list):
        for x in list:
            if x.name == name:
                return x




