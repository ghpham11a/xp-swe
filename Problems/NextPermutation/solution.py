class Solution(object):

    def next_permutation(self, nums):
        first_dec_index = len(nums) - 2
        
        while first_dec_index >= 0 and nums[first_dec_index + 1] <= nums[first_dec_index]:
            first_dec_index -= 1
            
        if first_dec_index >= 0:
            next_larger_index = len(nums) - 1
            while next_larger_index >= 0 and nums[next_larger_index] <= nums[first_dec_index]:
                next_larger_index -= 1
                
            self.swap(nums, first_dec_index, next_larger_index)
            
        self.reverse(nums, first_dec_index + 1)

    def reverse(self, nums, start):
        left = start
        right = len(nums) - 1
        
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1
        
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
solution = Solution()

test_input = [1,2,3]
solution.next_permutation(test_input)
assert(test_input == [1,3,2])

print("PASS")