class Solution:

    def max_sub_array(self, nums):
        best_sum = float("-inf")
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
            
        return best_sum

solution = Solution()

assert(solution.max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) == 6)

print("PASS")