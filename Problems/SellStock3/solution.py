class Solution(object):

    def max_profit(self, prices):
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:

            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit 

solution = Solution()

assert(solution.max_profit([3,3,5,0,0,3,1,4]) == 6)
assert(solution.max_profit([1,2,3,4,5]) == 4)

print("PASS")

