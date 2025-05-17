from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        # Iterate from the second-to-last house down to the first house
        for n in reversed(range(len(costs) - 1)):
            # Update the cost of painting house `n` red by adding the minimum cost of painting
            # house `n + 1` either green or blue (to avoid adjacent houses being the same color)
            costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])

            # Update the cost of painting house `n` green by adding the minimum cost of painting
            # house `n + 1` either red or blue
            costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])

            # Update the cost of painting house `n` blue by adding the minimum cost of painting
            # house `n + 1` either red or green
            costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])

        # The minimum cost to paint all houses is now stored in the first row;
        # return the smallest among red, green, and blue for the first house
        return min(costs[0])