"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

def max_sum(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]

    max_curr, total_max = arr[0], arr[0]
    for num in arr[1:]:
        max_curr = max(max_curr + num, num)
        total_max = max(total_max, max_curr)

    return total_max


print(max_sum([-2,1,-3,4,-1,2,1,-5,4]))

