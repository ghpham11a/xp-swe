class Solution:
    def rotate(self, nums, k):
        nums_len = len(nums) - 1

        self.reverse(0, nums_len, nums)

        k = k % len(nums)

        self.reverse(0, k - 1, nums)

        self.reverse(k, nums_len, nums)

    def reverse(self, start, end, nums):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp

            start += 1
            end -= 1