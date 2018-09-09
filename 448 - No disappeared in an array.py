"""

Given an array of integers where a[i] belongs to (1,n) (n = size of array),
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.

"""

def disappeared_num(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    return list((set(range(1,len(nums)+1))) - set(nums))

print(disappeared_num([4,3,2,7,8,2,3,1]))
