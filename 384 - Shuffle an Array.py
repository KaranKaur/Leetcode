"""

Shuffle a set of numbers without duplicates.

random.sample(population, k)

Return a k length list of unique elements chosen from the population sequence.
Used for random sampling without replacement.

"""
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = self.nums[:]  # copy the array into a new one
        for i in range(len(res) - 1, 0, -1):
            j = random.randrange(0, i + 1)
            res[i], res[j] = res[j], res[i]
        return res

    # Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()