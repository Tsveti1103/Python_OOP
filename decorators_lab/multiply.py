def multiply(times):
    def decorator(function):
        def wrapper(number):
            result = function(number) * times
            return result

        return wrapper

    return decorator


@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))

