class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a counter to store the number of set bits (1s)
        output = 0

        # Loop continues until all bits are shifted out (n becomes 0)
        while n:
            # n % 2 is equivalent to n & 1, returns 1 if the least significant bit is set
            output += n % 2

            # Right shift the bits of n by 1 to examine the next bit in the next iteration
            n = n >> 1

        # Return the total count of set bits (1s)
        return output