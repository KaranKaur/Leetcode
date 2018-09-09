"""

Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


"""

"""
p: parenthesis string built so far, 
left, right : number of left/right parenthesis still to add
paren: list to collect the parenthesis strings built
"""


def generate_paren(n):
    def gen_paren(p, left, right, paren=[]):
        if left:
            gen_paren(p + '(', left-1, right)
        if right > left:
            gen_paren(p + ')', left, right-1)

        if not right:
            paren += p,
        return paren

    return gen_paren("", n, n)


print(generate_paren(3))