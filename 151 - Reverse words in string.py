"""
Given an input string, reverse the string word by word.
"""

def rev_words(s):
    return " ".join(s.split(" ")[::-1])

print(rev_words("the sky is blue"))