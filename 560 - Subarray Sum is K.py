"""

Given an array of integers and an integer k, you need to find the total number of continuous
subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2


Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""

def subarray_sum(nums, k):
    count, res, curr = {0:1}, 0, 0
    for num in nums:
        curr += num
        res += count.get(curr-k, 0)
        count[curr] = count.get(curr, 0) + 1

    return res

print(subarray_sum([1,2,1,1,1], 2))

