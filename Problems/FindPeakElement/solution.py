class Solution(object):

    def find_peak_element(self, nums):
        
        start = 0
        end = len(nums) - 1
        
        while start < end:
            
            middle = start + (end - start) // 2
            
            if nums[middle] < nums[middle + 1]:
                start = middle + 1
            else:
                end = middle
                
        return start