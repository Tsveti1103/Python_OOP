def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for num in range(n):
            result.append(next(seq))
        return result
    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
