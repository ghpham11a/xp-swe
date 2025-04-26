class Solution:
    def removeDuplicates(self, nums):
        k = 0
        seen = {}

        for i in range(len(nums)):

            curr_num = nums[i]
            
            if curr_num not in seen or seen[curr_num] < 2:
                nums[k] = curr_num
                k += 1

                if curr_num not in seen:
                    seen[curr_num] = 1
                else:
                    seen[curr_num] += 1

        return k