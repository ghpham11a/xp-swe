class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Remove leading and trailing whitespace
        s = s.strip()

        # If the string is empty after trimming, return 0
        if not s:
            return 0

        sign = 1  # Default sign is positive
        result = 0  # This will store the numeric result

        # Step 2: Handle optional '+' or '-' sign
        if s[0] == "-" or s[0] == "+":
            if s[0] == "-":
                sign = -1  # Update sign if it's negative
            s = s[1:]  # Remove the sign character for digit parsing

        # Step 3: Convert digits until a non-digit character is found
        for char in s:
            if not char.isdigit():
                break  # Stop parsing when a non-digit is encountered
            result = result * 10 + int(char)  # Build the number from left to right

        # Step 4: Apply the sign
        result = result * sign

        # Step 5: Clamp the result to 32-bit signed integer range
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1

        # Step 6: Return the final integer
        return result