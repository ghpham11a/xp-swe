class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize the result variable that will hold the reversed bit sequence
        output = 0

        # Iterate over all 32 bits of the integer
        for i in range(32):
            # Extract the i-th bit from the input number 'n'
            # (n >> i) shifts 'n' right by 'i' bits, then '& 1' gets the least significant bit
            bit = (n >> i) & 1

            # Move the extracted bit to its reversed position in the output
            # (31 - i) computes the mirrored position in a 32-bit number
            output = output | (bit << (31 - i))

        # Return the final integer with bits reversed
        return output