""""
Given an integer array nums, find the contiguous subarray
within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 """

def max_product(arr):
    maximum_prod = big = small = arr[0]

    for num in arr[1:]:
        big, small = max(num, num*big, num*small), min(num, num*big, num*small)
        maximum_prod = max(maximum_prod, big)
    return maximum_prod

print(max_product([-2,0,-1]))