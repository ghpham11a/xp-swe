class Solution:

    def jump(self, nums):
        
         # Counts the number of jumps needed to reach the end
        output = 0
        # The last index we need to reach
        target_index = len(nums) - 1
        # The start of the current range of reachable indices
        left = 0
        # The end of the current range of reachable indices
        right = 0 

        # Continue jumping until our range includes the last index
        while right < target_index:
            farthest = 0  # Tracks the farthest index we can reach in the next jump

            # Check all indices in the current range [left, right]
            for i in range(left, right + 1):
                # Update the farthest we can go from the current index
                farthest = max(farthest, i + nums[i])

            # Move to the next jump:
            # left becomes the index right after the current range
            left = right + 1
            # right becomes the farthest point we can reach
            right = farthest

            # We made one jump
            output += 1
            
        return output

solution = Solution()

assert(solution.insert([2,3,1,1,4]) == 2)

print("PASS")