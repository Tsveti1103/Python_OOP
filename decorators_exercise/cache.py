def cache(func):
    log = {}

    def wrapper(num):
        # check if this number is already calculated and in log(5 = 4+3 - we already have calculated 4 and 3)
        if num in log:
            return log[num]
        else:
            log[num] = func(num)
            return log[num]

    # make log property to wrapper>cache>fibonacci - now we can call log from fibonacci -  fibonacci.log
    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
