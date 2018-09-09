class Solution(object):

    @staticmethod
    def range_bitwise_and(self, m, n):
        i = 0
        while m < n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i

    # If m is no longer smaller than n, and is equal, then the bitwise & of
    # these two number is the number itself (n). So all you need to return is
    #  the number n by the end, but shifted to the left by i bits,
    # corresponding to the number of bits you had to move m and n so that
    # they become equal.

    # https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56719/JavaPython-easy-solution-with-explanation
    
