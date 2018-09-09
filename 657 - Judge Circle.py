"""

Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.

Example:
Input: "UD"
Output: true

Input: "LL"
Output: false

"""
from time import time

def judge_circle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    x = y = 0
    t1 = time()
    for move in moves:
        if move == 'U': y -= 1
        elif move == 'D': y += 1
        elif move == 'L': x -= 1
        elif move == 'R': x += 1
    t2 = time()
    print('Method 1, time: %f'%(t2-t1))
    return x == y == 0

def judge_circle2(moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
