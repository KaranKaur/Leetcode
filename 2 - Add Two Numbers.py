"""

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


def add_two_num(l1, l2):
    if not l1 or not l2:
        return l1 or l2

    def to_int(node):
        return node.val + 10 * to_int(node.next) if node else 0

    n = to_int(l1) + to_int(l2)
    first = last = ListNode(n % 10)
    while n > 9:
        n /= 10
        last.next = last = ListNode(n % 10)
    return first


