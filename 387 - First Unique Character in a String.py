"""

Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Example:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

"""

def first_uniq_char(s):
    """
    :type s: str
    :rtype: int
    """

    letters = 'abcdefghijklmnopqrstuvwxyz'
    idx = [s.index(l) for l in letters if s.count(l) == 1]
    return min(idx) if len(idx) > 0 else -1
