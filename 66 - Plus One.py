"""

Given a non-empty array of digits representing a non-negative integer,
plus one to the integer.

The digits are stored such that the most significant digit is at the
head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero,
except the number 0 itself.

"""

def plus_one(nums):
    sum_nums = 0
    for i in range(len(nums)):
        sum_nums += nums[i] * (10**(len(nums)-i-1))
    return [int(i) for i in str(sum_nums+1)]


print(plus_one([1,2,3]))
#[1, 2, 4]

