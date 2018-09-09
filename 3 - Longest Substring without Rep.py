"""

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
 Note that the answer must be a substring, "pwke" is a subsequence and not
a substring.


O(n) solution, using a dictionary
"""

def long_repeat_substring(s):
    max_len = start = 0
    char_dict = {}

    for i in range(len(s)):
        if s[i] in char_dict and start <= char_dict[s[i]]:
            start = char_dict[s[i]] + 1
        else:
            max_len = max(max_len, i - start + 1)
        char_dict[s[i]] = i

    return max_len

print(long_repeat_substring("abcabcbb"))
