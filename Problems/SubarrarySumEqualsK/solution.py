from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0  # To store the total number of valid subarrays
        curr_sum = 0  # Running prefix sum of elements

        sum_map = {}  # Dictionary to store the frequency of prefix sums
        sum_map[0] = 1  # Base case: one way to have a sum of 0 (empty subarray before any element)

        for i in range(len(nums)):
            curr_sum += nums[i]  # Update the running sum to include the current element

            other_sum = curr_sum - k  # The sum we need to find in the past to make a subarray sum to k

            # If that required sum has been seen before, it means there are subarrays ending at i with sum k
            if other_sum in sum_map:
                count += sum_map[other_sum]

            # Update the frequency of the current running sum in the map
            if curr_sum in sum_map:
                sum_map[curr_sum] += 1
            else:
                sum_map[curr_sum] = 1

        return count  # Return the total number of subarrays with sum equal to k