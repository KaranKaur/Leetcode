""""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.


example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # convert l1 and l2 into integers, then add and make a linked list of out it

        def to_int(node):
            int_val = 0
            while node:
                int_val = int_val * 10 + node.val
                node = node.next
            return int_val

        num = to_int(l1) + to_int(l2)

        first = ListNode(0)
        if num == 0:
            return first
        while num:
            val, num = num % 10, num / 10
            first.next, first.next.next = ListNode(val), first.next

        return first.next




