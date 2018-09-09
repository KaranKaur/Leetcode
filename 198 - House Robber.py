# coding=utf-8
"""

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses were
broken into on the same night.

Given a list of non-negative integers representing the amount of money of
each house, determine the maximum amount of money you can rob tonight without
alerting the police.

Example:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

f(k) = Largest amount that you can rob from the first k houses.
Ai = Amount of money at the ith house.

Let us look at the case n = 1, clearly f(1) = A1.

Now, let us look at n = 2, which f(2) = max(A1, A2).

For n = 3, you have basically the following two options:

Rob the third house, and add its amount to the first house's amount.

Do not rob the third house, and stick with the maximum amount of
the first two houses.

"""

#f(k) = max(f(k – 2) + Ak, f(k – 1))

nums = [1,2,3]

def house_rob(nums):
    prev = curr = 0
    for i in nums:
        prev, curr = curr, max(prev + i, curr)
    return curr

print(house_rob([2,7,9,3,1]))
