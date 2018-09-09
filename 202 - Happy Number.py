"""

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares
of its digits, and repeat the process until the number equals 1 (where it will stay), or
it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.


#to check for the loops, not ending in 1 => the same numbers will keep on coming up,
so we should some data structure that will help us, to have only unique numbers!
which is SET
"""
def happy_number(n):
    seen = set()
    while n not in seen:
        seen.add(n) # set does not have 'APPEND'
        n = sum([int(i) ** 2 for i in str(n)])
    return n == 1

print(happy_number(19))
#True