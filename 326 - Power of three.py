"""

Given an integer, write a function to determine if it is a power of three.

"""

def pow_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n /= 3
    return True if n == 1 else False

print(pow_three(81))
print(pow_three(30))