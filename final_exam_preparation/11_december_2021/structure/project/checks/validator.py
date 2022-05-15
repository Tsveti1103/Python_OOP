class Validator:
    @staticmethod
    def string_len_more_then(text, num, message):
        if len(text) < num:
            raise ValueError(message)
        return text

    @staticmethod
    def check_empty_string(text, message):
        if text.strip() == "":
            raise ValueError(message)
        return text
