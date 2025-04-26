class Solution:

    def can_jump(self, nums):
        
        # Start by setting the target to the last index
        # Our goal is to work backwards and see if we can reach this target
        target = len(nums) - 1

        # Iterate from the end of the list to the beginning
        for i in range(len(nums) - 1, -1, -1):
            # If from the current position `i`, we can jump to (or beyond) the current target
            if i + nums[i] >= target:
                # Then update the target to the current position
                # This means: "now I only need to check if I can reach position i"
                target = i

        # After the loop, if we've moved the target all the way back to index 0,
        # it means we can reach the end from the start
        return target == 0


solution = Solution()

assert(solution.insert([2,3,1,1,4]) == True)

print("PASS")