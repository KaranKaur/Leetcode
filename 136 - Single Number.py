"""
Given a non-empty array of integers,
every element appears twice except for one. Find that single one.
"""

from collections import Counter

def single_number(nums):
    counts = Counter(nums)
    for k, v in counts.items():
        if v == 1:
            return k


print(single_number([4,1,2,1,2]))