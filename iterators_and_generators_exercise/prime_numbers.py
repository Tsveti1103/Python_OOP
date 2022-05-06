# def get_primes(nums):
#     for num in nums:
#         count = 0
#         for d in range(2, num):
#             if num % d == 0:
#                 count += 1
#         if count < 1 < num:
#             yield num

def is_prime(num):
    return num > 1 and all(num % i for i in range(2, num))


def get_primes(nums):
    primes = filter(lambda n: is_prime(n), nums)
    for num in primes:
        yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
print(list(get_primes([7])))
