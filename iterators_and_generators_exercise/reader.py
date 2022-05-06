def read_next(*args):
    for current_iterable in args:
        for item in current_iterable:
            yield item


for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
    print(item, end='')
