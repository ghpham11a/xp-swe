class Solution(object):

    def max_profit(self, prices):

        min_price = prices[0]
        max_profit = 0

        for price in prices:

            min_price = min(min_price, price)

            current_profit = price - min_price

            max_profit = max(max_profit, current_profit)
            
        return max_profit

solution = Solution()

assert(solution.max_profit([7,1,5,3,6,4]) == 5)

print("PASS")