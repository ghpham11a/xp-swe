class Solution(object):

    def max_profit(self, prices):

        # t1_cost: Minimum price to buy the first stock (first transaction).
        # t2_cost: Effective minimum cost for the second transaction, adjusted by the profit from the first transaction.
        t1_cost, t2_cost = float('inf'), float('inf')

        # t1_profit: Maximum profit achievable with one transaction.
        # t2_profit: Maximum profit achievable with at most two transactions.
        t1_profit, t2_profit = 0, 0

        # Loop through each price in the list.
        for price in prices:

            # Update the minimum cost for the first transaction.
            # This finds the best (lowest) buying price so far.
            t1_cost = min(t1_cost, price)

            # Calculate the profit if we sold at the current price for the first transaction.
            # Then update the maximum profit so far.
            t1_profit = max(t1_profit, price - t1_cost)

            # For the second transaction, we effectively 'reduce' the cost by the profit from the first transaction.
            # This adjustment allows us to simulate reinvesting the gains from the first transaction.
            t2_cost = min(t2_cost, price - t1_profit)

            # Calculate the maximum profit if we sold at the current price for the second transaction.
            # This profit is the net gain considering both transactions.
            t2_profit = max(t2_profit, price - t2_cost)

        # The maximum profit achievable with at most two transactions is stored in t2_profit.
        return t2_profit 

solution = Solution()

assert(solution.max_profit([3,3,5,0,0,3,1,4]) == 6)
assert(solution.max_profit([1,2,3,4,5]) == 4)

print("PASS")