"""

Search a 2D matrix,
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
    1) Integers in each row are sorted from left to right.
    2) The first integer of each row is greater than the last integer of the
    previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

"""
def search_2D_matrix(matrix, target):
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    rows , cols = len(matrix), len(matrix[0])
    low , high = 0, rows * cols - 1
    while low <= high:
        mid = (low + high) / 2
        num = matrix[mid/cols][mid%cols]

        if num == target:
            return True
        elif num < target:
            low = mid + 1
        elif num > target:
            high = mid - 1
    return False


m = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 3
print(search_2D_matrix(m, target))