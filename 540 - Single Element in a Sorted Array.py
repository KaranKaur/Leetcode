"""

Given a sorted array consisting of only integers where every element appears
twice except for one element which appears once. Find this single element that
appears only once.


Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
Binary Search

USe XOR: since you want pairs, (0,1), (2,3) etc
"""

#O(log(n))
def single_ele(nums):
    lo, hi = 0, len(nums)-1
    while lo < hi:
        mid = (lo + hi )/2
        if nums[mid] == nums[mid^1]:
            lo = mid + 1
        else:
            hi = mid

    return nums[lo]

x = [3,3,7,7,10,11,11]
print(single_ele(x))


#O(n) - dict construction
def two(nums):
    dict_temp = {}
    for i in nums:
        dict_temp[i] = dict_temp.get(i, 0) + 1

    for k, v in dict_temp.items():
        if v == 1:
            return k


print(two(x))