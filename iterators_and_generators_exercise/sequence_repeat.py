class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.sequence) < self.number:
            self.sequence = self.sequence + self.sequence

        else:
            while self.number > 0:
                self.number -= 1
                current = self.sequence[0]
                self.sequence = self.sequence[1::]
                return current
            else:
                raise StopIteration()
