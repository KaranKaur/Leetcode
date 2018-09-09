"""

Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""
def three_sum(nums):
    res = [] # to hold the results
    nums.sort() # sort the input array in place

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: # check the duplicates
            continue
        l, r = i+1, len(nums)-1

        while l < r:
            temp_sum = nums[i] + nums[l] + nums[r]
            if temp_sum < 0:
                l += 1
            elif temp_sum > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and  nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r-=1
    return res

x = [-1, 0, 1, 2, -1, -4]
print(three_sum(x))
