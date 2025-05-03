class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize the output string to build the result, and a carry variable for binary addition
        output = ""
        carry = 0

        # Reverse both strings to make addition easier (starting from least significant bit)
        a, b = a[::-1], b[::-1]

        # Loop through the longest string's length
        for i in range(max(len(a), len(b))):
            # Get the digit from 'a' at position i if it exists, otherwise use 0
            digit_a = ord(a[i]) - ord("0") if i < len(a) else 0
            # Get the digit from 'b' at position i if it exists, otherwise use 0
            digit_b = ord(b[i]) - ord("0") if i < len(b) else 0

            # Calculate total sum of the digits and the carry
            total = digit_a + digit_b + carry
            # The binary digit to add to result is total % 2 (either 0 or 1)
            char = str(total % 2)
            # Prepend the calculated binary digit to the output
            output = char + output
            # Update carry (0 or 1) for the next iteration
            carry = total // 2

        # If there's still a carry left after the loop, prepend '1' to the result
        if carry:
            output = "1" + output

        # Return the final binary string result
        return output
