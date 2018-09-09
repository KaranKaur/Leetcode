"""

Given two lists A and B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the
order of the elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

These lists A and B may contain duplicates. If there are multiple answers, output any of them.

Example:
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
Output : [1, 4, 3, 2, 0]

"""
def anagram_mapping(A, B):
    res = []
    for num in A:
        if num in B:
            idx = B.index(num)
            res.append(idx)
    return res


x = [12, 28, 46, 32, 50]
y = [50, 12, 32, 46, 28]
print(anagram_mapping(x,y))

