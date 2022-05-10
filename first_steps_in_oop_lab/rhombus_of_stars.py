def print_parts(n, r):
    print(" "*(n-r), end="")
    for star in range(1, r):
        print('*', end=" ")
    print("*")


def first_part(n):
    for row in range(1, n + 1):
        print_parts(n, row)


def second_part(n):
    for row in range(n-1, 0, -1):
        print_parts(n, row)


def result(n):
    first_part(n)
    second_part(n)


n = int(input())
result(n)
