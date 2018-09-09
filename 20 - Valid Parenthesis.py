"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:

1) Open brackets must be closed by the same type of brackets.
2) Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false,

Input: "([)]"
Output: false

Example 4:
Input: "{[]}"
Output: true

"""
def valid_paren(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    char_dict = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char in char_dict.values():
            stack.append(char)
        elif char in char_dict.keys():
            if stack == [] or char_dict[char] != stack.pop():
                return False
        else:
            return False

    return stack == []

print(valid_paren("([)]"))
print(valid_paren("()[]{}"))