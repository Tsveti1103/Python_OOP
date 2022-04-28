def type_check(given_type):
    def decorator(func):
        def wrapper(arg):
            if type(arg) == given_type:
                return func(arg)
            else:
                return 'Bad Type'

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

