"""

Given a non-empty integer array of size n, find the minimum number of moves required
to make all array elements equal,
where a move is incrementing n - 1 elements by 1.

Example:
Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

Logic:
Incrementing all but one is equivalent to decrementing that one. So let's do that
instead. How many single-element decrements to make all equal? No point to
decrementing below the current minimum, so how many single-element decrements to
make all equal to the current minimum? Just take the difference from what we
currently have (the sum) to what we want (n times the minimum).


"""
def min_moves(nums):
    return sum(nums) - min(nums)*len(nums)