"""

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.


addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

#use heaps!
Default is min heap in python
Keeping the entire input sorted is not required, so we just need top elements
Take two heaps: one - a min heap, we will store the larger elements - and
top element will be the minimum of all,
another will be the max heap, where we will store the smaller section of nums
top will be the maximum of those number.

"""

from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))


    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        else:
            return (large[0] - small[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()