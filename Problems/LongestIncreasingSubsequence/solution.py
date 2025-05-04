class Solution(object):

    def length_of_lis(self, nums):
        # Create a table where table[i] will store the length of the longest increasing subsequence
        # that ends with nums[i]. Initialize all values to 1 since the minimum LIS at each index is 1 (the element itself).
        dp = [1] * len(nums)

        # Start from the second element and compare it with all previous elements.
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                # If current number nums[i] is greater than nums[j], it means we can extend the
                # increasing subsequence ending at index j.
                if nums[i] < nums[j]:
                    # Update table[i] with the maximum of its current value or the length of subsequence
                    # ending at j plus 1 (including nums[i]).
                    dp[i] = max(dp[i], dp[j] + 1)

        # The result is the maximum value in the table, which represents the length of the
        # longest increasing subsequence in the entire array.
        return max(dp)

solution = Solution()

assert(solution.length_of_lis([10,9,2,5,3,7,101,18]) == 4)

print("PASS")