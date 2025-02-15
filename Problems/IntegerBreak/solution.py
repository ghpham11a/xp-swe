class Solution:
    
    def integer_break(self, n):
        if n <= 3:
            return n - 1
        
        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
            
        for num in range(4, n + 1):
            ans = num
            for sub_num in range(2, num):
                ans = max(ans, sub_num * dp[num - sub_num])
            
            dp[num] = ans
        
        return dp[-1]