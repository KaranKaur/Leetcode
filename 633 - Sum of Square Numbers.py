"""

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5


Example 2:
Input = 3
Output = False

Important condition to meet is 0 < a< sqrt(c)
any() in python returns true if any element in the iterable is True
"""


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        def is_sq(n):
            return int(n ** .5) ** 2 == n

        return any(is_sq(c - a * a) for a in range(int(c ** .5 + 1)))