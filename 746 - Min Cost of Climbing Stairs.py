"""

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps.
You need to find minimum cost to reach the top of the floor,
and you can either start from the step with index 0, or the step with index 1.

Example:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.


Example:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
"""

def min_cost(cost):

    min_cost0, min_cost1 = cost[0], cost[1]
    for i in range(2, len(cost)):
        min_cost0, min_cost1 = min_cost1, min(min_cost0, min_cost1) + cost[i]
    return min(min_cost0, min_cost1)

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(min_cost(cost))