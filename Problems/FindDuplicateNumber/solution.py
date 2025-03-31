class Solution(object):

    def find_duplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        while fast and nums[fast] is not None:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break 

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

solution = Solution()

assert(solution.find_duplicate([1,3,4,2,2]) == 2)
assert(solution.find_duplicate([3,1,3,4,2]) == 3)

print("PASS")