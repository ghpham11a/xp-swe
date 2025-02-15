class Solution:

    def largest_perimeter(self, nums):
        
        nums.sort()
        output = -1
        total = 0

        for num in nums:
            if total > num:
                output = total + num
            total += num

        return output