class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.x = len(iterable)-1

    def __iter__(self):
        return self

    def __next__(self):
        while self.x >= 0:
            current = self.iterable[self.x]
            self.x -= 1
            return current
        else:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
