class Solution:
    
    def integer_break(self, n):
        # For n <= 3, we must break it into at least two positive integers
        # So the maximum product is n - 1
        if n <= 3:
            return n - 1
        
        # Initialize a DP array where dp[i] will store the max product for integer i
        dp = [0] * (n + 1)

        # Base cases: for 1, 2, and 3, the max product without forcing a break is the number itself
        dp[1] = 1
        dp[2] = 2  # Even though integer break of 2 is 1+1, setting 2 helps with multiplication in recursion
        dp[3] = 3  # Same reasoning: set dp[3] = 3 to make recursive product calculations easier

        # Fill in the DP table from 4 to n
        for num in range(4, n + 1):
            ans = num  # Initialize the best product as num itself, to be updated
            for sub_num in range(2, num):
                # Try breaking `num` into `sub_num + (num - sub_num)`
                # Use the precomputed best product for (num - sub_num)
                ans = max(ans, sub_num * dp[num - sub_num])
            
            # Store the maximum product for `num`
            dp[num] = ans
        
        # Return the max product for n
        return dp[-1]