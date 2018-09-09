"""

Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example:
Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121.
From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""

def if_palin_num(x):
    if x < 0:
        return False
    x = str(x)
    left, right = 0, len(x) - 1
    while left <= right:
        if x[left] == x[right]:
            left += 1;
            right -= 1
        else:
            return False
    return True

def if_palin(x):
    return False if x < 0 else int(str(x)[::-1]) == x