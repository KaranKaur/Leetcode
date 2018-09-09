"""

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

    1) Integers in each row are sorted in ascending from left to right.
    2) Integers in each column are sorted in ascending from top to bottom.

Example:
Matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.

#can not apply binary search here.

Here we start the search from top right
"""
def search_2D_matrix_2(matrix, target):
    if not matrix or target is None:
        return False

    rows, cols = len(matrix), len(matrix[0])
    r, c = 0, cols-1

    while r < rows and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1
        else:
            r += 1
    return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(search_2D_matrix_2(matrix, 5))
print(search_2D_matrix_2(matrix, 20))
print(search_2D_matrix_2(matrix, 0))
