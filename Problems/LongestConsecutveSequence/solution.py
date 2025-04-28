from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0  # Initialize the maximum streak length found
        
        num_set = set(nums)  # Put all numbers into a set for O(1) lookups
        
        for num in num_set:  # Iterate through each unique number
            # Only start counting if `num` is the start of a sequence
            # (i.e., there is no number before it)
            if num - 1 not in num_set:
                current_num = num  # Start of a new sequence
                current_streak = 1  # The current sequence length

                # Keep checking if the next number exists in the set
                while current_num + 1 in num_set:
                    current_num += 1  # Move to the next consecutive number
                    current_streak += 1  # Increase the current sequence length

                # Update the longest streak if the current one is longer
                longest_streak = max(longest_streak, current_streak)

        return longest_streak  # Return the length of the longest consecutive sequence