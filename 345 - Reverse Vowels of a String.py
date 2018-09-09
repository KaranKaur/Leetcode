"""

Write a function that takes a string as input and reverse only the vowels of a string.

Example:
Given s = "hello", return "holle".

Example:
Given s = "leetcode", return "leotcede".

"""

from time import time

def rev_vowels(s):
    t1 = time()
    vowels = set(list('aeiouAEIOU'))
    s = list(s)

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        elif s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1; right -= 1
    t2 = time()
    print('Time taken: %f'%(t2-t1))
    return "".join(s)

print(rev_vowels("leetcode"))
#with list: Time taken: 0.000047
#With Set : Time taken: 0.000016: Lookup faster in set than in lists