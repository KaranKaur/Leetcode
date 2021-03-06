"""

Given a positive integer n, generate a square matrix filled with elements from
1 to n square in spiral order.

n , n square = n * n matrix

"""
def generateMatrix(n):
    A, lo = [], n*n+1
    while lo > 1:
        lo, hi = lo - len(A), lo
        A = [range(lo, hi)] + zip(*A[::-1])
    return A

generateMatrix(2)
