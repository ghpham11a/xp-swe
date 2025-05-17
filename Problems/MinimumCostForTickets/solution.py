from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Dictionary to store the minimum cost from day i to the end
        dp = {}

        # Iterate backwards through the days list
        for i in range(len(days) - 1, -1, -1):
            # Initialize with a high value to find the minimum later
            dp[i] = float("inf")
            
            # Try each type of ticket: 1-day, 7-day, and 30-day
            for d, c in zip([1, 7, 30], costs):
                j = i

                # Find the next index j such that the current pass would not cover day[j]
                # This loop skips all days that are covered by the current pass (starting from days[i])
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                
                # Recurrence relation:
                # dp[i] is the minimum of its current value and the cost of this pass
                # plus the cost to cover the remaining days starting at index j
                dp[i] = min(dp[i], c + dp.get(j, 0))

        # Return the minimum cost to cover all days starting from index 0
        return dp[0]