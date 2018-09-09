""""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Basically grow it from middle to left and right

This is a DP solution, with O(n^2) time complexity and O(1) extra space

Idea: Expand around the center
we could solve it in O(n^2) time using only constant space.

We observe that a palindrome mirrors around its center.
Therefore, a palindrome can be expanded from its center, and
there are only 2n - 1 such centers.

You might be asking why there are 2n - 1 but not n centers?
The reason is the center of a palindrome can be in between two letters.
Such palindromes have even number of letters (such as "abba") and
its center are between the two bs.

Time complexity : O(n^2)
Since expanding a palindrome around its center could take O(n) time,
the overall complexity is O(n^2).

Space complexity : O(1).

"""

#this function, basically grows the palindrome and checks
def get_palindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]

#call this function for each index i in string s, and update res if longer
#plaindrome sequnece is found.

def longest_palindrome(s):
    res = ""
    for i in range(len(s)):

        #odd case: 'aba'
        odd_palin = get_palindrome(s, i, i)
        if len(odd_palin) > len(res):
            res = odd_palin
        #even case: 'abba'
        even_palin = get_palindrome(s, i, i+1)
        if len(even_palin) > len(res):
            res = even_palin

    return res
