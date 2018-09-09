"""
49
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Defaultdict = Gives a default for a non existant key value, no KeyError.
Any key that does not exist gets the value returned by the default factory.

All inputs will be in lowercase.
The order of your output does not matter.
"""
import collections
def group_anagrams(strs):

    res = collections.defaultdict(list)
    for s in strs:
        res[tuple(sorted(s))].append(s)
    return res.values()

x = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(x))
