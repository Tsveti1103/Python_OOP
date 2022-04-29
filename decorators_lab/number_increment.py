def number_increment(numbers):
    def increase():
        result = [num + 1 for num in numbers]
        return result

    return increase()


print(number_increment([1, 2, 3]))
