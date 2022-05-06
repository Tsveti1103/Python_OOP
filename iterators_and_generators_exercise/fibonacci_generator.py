def fibonacci():
    fn_1 = 0
    fn_2 = 1
    yield fn_1
    yield fn_2
    while True:
        fn = fn_1 + fn_2
        yield fn
        fn_1 = fn_2
        fn_2 = fn


generator = fibonacci()
for i in range(5):
    print(next(generator))
