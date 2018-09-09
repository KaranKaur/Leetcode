"""

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Example:
n = 3

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

def gen_paren(n):

    def generate_paren(p, left, right, paren = []):
        if left:
            generate_paren(p + '(', left-1, right)
        if right > left:
            generate_paren(p + ')', left, right-1)
        if not right:
            paren += p,
        return paren

    return generate_paren('', n, n)

gen_paren(3)