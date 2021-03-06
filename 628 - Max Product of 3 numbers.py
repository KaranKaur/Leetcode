"""

Given an integer array,
find three numbers whose product is maximum and output the maximum product.


Example 1:
Input: [1,2,3]
Output: 6

Example 2:
Input: [1,2,3,4]
Output: 24

"""

def max_product_3(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

print(max_product_3([1,2,3,4]))
print(max_product_3([1,2,3]))