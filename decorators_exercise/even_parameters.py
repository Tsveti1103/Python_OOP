def even_parameters(func):
    def wrapper(*args):
        for num in args:
            if not isinstance(num, int) or num % 2 != 0:
                return "Please use only even numbers!"

        return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))


