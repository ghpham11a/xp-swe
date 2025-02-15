class Solution(object):

    def maxProfit(self, prices):
        output = 0

        for index in range(1, len(prices)):
            if prices[index] > prices[index - 1]:
                output += (prices[index] - prices[index - 1])

        return output

solution = Solution()

assert(solution.max_profit([7,1,5,3,6,4]) == 7)

print("PASS")