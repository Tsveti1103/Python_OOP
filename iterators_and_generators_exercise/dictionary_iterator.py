class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.i = len(dictionary) - 1
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i >= 0:
            self.i -= 1
            self.n += 1
            for i, v in self.dictionary.items():
                self.dictionary.pop(i)
                return i, v
        else:
            raise StopIteration


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

