class Solution:

    def max_profit(self, prices, fee):
        
        n = len(prices)
        
        # 'hold' represents the max profit if we currently hold a stock.
        # We initialize it to -prices[0] because we buy the stock on day 0.
        hold = -prices[0]
        
        # 'free' represents the max profit if we currently do not hold a stock.
        # Initially, we don't hold any stock, so the profit is 0.
        free = 0
        
        for i in range(1, n):
            # Save the current value of hold before updating it,
            # because we will use the old 'hold' value to update 'free'.
            tmp = hold
            
            # Update 'hold' to be the maximum of:
            # 1. Keeping the stock we already hold (i.e., do nothing).
            # 2. Buying a new stock today, which means we must be in 'free' state yesterday
            #    and then subtract today's price to buy.
            hold = max(hold, free - prices[i])
            
            # Update 'free' to be the maximum of:
            # 1. Staying in the 'free' state (i.e., do nothing).
            # 2. Selling the stock we held yesterday at today's price, and paying the transaction fee.
            free = max(free, tmp + prices[i] - fee)
        
        # Return the maximum profit when we do not hold any stock
        # (because holding stock at the end doesn't realize the profit).
        return free