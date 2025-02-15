class Solution:
    def reverse(self, x):
        
        MAX = (2**31) - 1
        MIN = -2**31
        MAX_TRIMMED = MAX // 10
        MIN_TRIMMED = math.ceil(MIN / 10)

        output = 0
        
        while x:

            if x >= 0:   
                digit = x % 10
            else:
                digit = (abs(x) % 10) * -1

            if x >= 0:
                x = x // 10
            else:
                x = math.ceil(x / 10)

            if (output > MAX_TRIMMED) or (output == MAX_TRIMMED and digit > 7):
                return 0
            
            if (output < MIN_TRIMMED) or (output == MIN_TRIMMED and digit < -8):
                return 0
            
            output = output * 10 + digit
        
        return output

solution = Solution()

assert(solution.reverse(123) == 321)

print("PASS")