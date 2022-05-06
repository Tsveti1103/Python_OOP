class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count > 0:
            current = self.i
            self.i += self.step
            self.count -= 1
            return current

        else:
            raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
