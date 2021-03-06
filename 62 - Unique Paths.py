"""

A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in
the diagram below).

How many possible unique paths are there?

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28

"""

def unique_paths(m, n):
    aux = [[1 for x in range(n)] for x in range(m)]

    for i in range(1, m):
        for j in range(1,n):
            aux[i][j] = aux[i-1][j] + aux[i][j-1]

    return aux[-1][-1]

print(unique_paths(7,3))