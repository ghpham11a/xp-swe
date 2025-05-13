class Solution:
    # Generalized k-sum function (used recursively)
    def k_sum(self, nums, target, k):
        output = []
        
        # Base case: if array is empty, return no results
        if not nums:
            return output
        
        # Base case: 2-sum is solved with a two-pointer approach
        if k == 2:
            return self.two_sum(nums, target)

        # Recursive case: reduce k-sum to (k-1)-sum
        for i in range(len(nums)):
            # Skip duplicates to avoid repeating quadruplets
            if i == 0 or nums[i - 1] != nums[i]:
                # Recursively find (k-1)-sized subsets from the rest of the array
                # that sum to (target - nums[i])
                for subset in self.k_sum(nums[i + 1:], target - nums[i], k - 1):
                    # Prepend the current element to each valid subset
                    output.append([nums[i]] + subset)

        return output

    # Two-pointer approach to find all unique pairs that sum to target
    def two_sum(self, nums, target):
        output = []
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            curr_sum = nums[lo] + nums[hi]
            # If sum is too small or left is a duplicate, move left pointer forward
            if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                lo += 1
            # If sum is too large or right is a duplicate, move right pointer backward
            elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                # Valid pair found
                output.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1

        return output

    # Main function to be called for 4Sum problem
    def four_sum(self, nums, target):
        # Sort array to handle duplicates and enable two-pointer logic
        nums.sort()
        # Call the generalized k-sum with k=4
        return self.k_sum(nums, target, 4)

runner = Solution()

assert(runner.four_sum([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])

print("PASS")