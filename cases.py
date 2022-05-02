#!/usr/bin/env python3
from unittest import case
from setup import *


def adjacent(a: int, b: int) -> bool:
    if a == b:
        return False
    small = min(a, b)
    big = max(a, b)

    if big > 3 and small < 4:
        return big % 4 == small
    
    small = small % 4
    big = big % 4

    return (small + 1) % 4 == big or (big + 1) % 4 == small


def opposite(a: int, b: int) -> bool:
    if a == b:
        return False
    small = min(a, b)
    big = max(a, b)

    if big > 3 and small < 4:
        return (small + 2) % 4 == big - 4

    return False


def num_adjacent(nums: list) -> int:
    val = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if adjacent(nums[i], nums[j]):
                val += 1
    return val


def num_opposite(nums: list) -> int:
    val = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if opposite(nums[i], nums[j]):
                val += 1
    return val


def get_nums(x):
    nums = []

    for i in range(8):
        if x & (1 << i):
            nums.append(i)
    
    inverted = len(nums) > 4
    if inverted:
        nums.clear()
        for i in range(8):
            if not (x & (1 << i)):
                nums.append(i)

    return nums, inverted




def get_case(x: int) -> int:
    nums, _ = get_nums(x)
    n = len(nums)
    adj_opp = (num_adjacent(nums), num_opposite(nums))

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        if (adj_opp) == (1, 0):
            return 2
        elif (adj_opp) == (0, 0):
            return 3
        elif (adj_opp) == (0, 1):
            return 4
    elif n == 3:
        if (adj_opp) == (2, 0):
            return 5
        elif (adj_opp) == (1, 1):
            return 6
        elif (adj_opp) == (0, 0):
            return 7
    elif n == 4:
        if (adj_opp) == (4, 0):
            return 8
        elif (adj_opp) == (3, 0):
            return 9
        elif (adj_opp) == (2, 2):
            return 10
        elif (adj_opp) == (3, 1):
            return 11
        elif (adj_opp) == (2, 1):
            return 12
        elif (adj_opp) == (0, 0):
            return 13
    

    return -1

"""
print('{', end='')
for i in range(256):
    print(getcase(i), end=', ')
    if i % 16 == 15:
        print('')
print('}', end='')
"""
