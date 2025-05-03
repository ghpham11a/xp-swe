class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize the result variable to 0
        output = 0

        # Iterate through each number in the array
        for n in nums:
            # XOR the current number with the result
            # Numbers appearing twice will cancel out (n ^ n = 0)
            # The number appearing once will remain
            output = n ^ output

        # Return the number that appears only once
        return output