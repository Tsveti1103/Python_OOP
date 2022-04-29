def vowel_filter(function):
    def wrapper():
        letters = [letter for letter in function() if letter.lower() in 'aioweuy']
        return letters

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
