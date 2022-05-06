# def all_permutations(seq):
#     if len(seq) == 0:
#         return []
#
#     if len(seq) == 1:
#         return [seq]
#
#     l = []
#     for i in range(len(seq)):
#         m = seq[i]
#
#         rem_list = seq[:i] + seq[i + 1:]
#
#         for p in all_permutations(rem_list):
#             l.append([m] + p)
#     return l
#
#
# def possible_permutations(seq):
#     perms = all_permutations(seq)
#     for pers in perms:
#         yield pers
import itertools


def possible_permutations(seq):
    perms = itertools.permutations(seq)
    for pers in perms:
        yield list(pers)



[print(n) for n in possible_permutations([1, 2, 3])]
