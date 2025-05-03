class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0  # Counter to track how many bits we've shifted

        # Keep shifting both left and right until they are equal
        # This finds the common prefix of left and right in binary
        while left != right:
            left = left >> 1    # Right shift both numbers to eliminate differing bits
            right = right >> 1
            i += 1              # Track how many shifts we've done

        # Shift the result back to the left to restore the zeroed-out bits
        return left << i