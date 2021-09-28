from itertools import permutations
def permute(nums):
    return list(map(list, permutations(nums)))
