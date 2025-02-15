class Solution:

    def max_strength(self, nums):

        if len(nums) == 1:
            return nums[0]
        
        pos = []
        neg = []
 
        for num in nums:
            if num < 0:
                neg.append(num)
            elif num > 0:
                pos.append(num)

        if len(neg) % 2 == 1:
            neg.remove(max(neg))

        if not pos and not neg:
            return 0
        
        return prod(pos) * prod(neg)

solution = Solution()

assert(solution.max_strength([3,-1,-5,2,5,-9]) == 1350)

print("PASS") 