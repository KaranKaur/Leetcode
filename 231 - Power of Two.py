"""

Given an integer, write a function to determine if it is a power of two.

Example:
Input: 1
Output: true

Input: 16
Output: true

Input: 218
Output: false

"""
def pow_two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n /= 2
    return True if n == 1 else False

print(pow_two(218))
print(pow_two(0))