class Solution:

    def getSum(self, a: int, b: int) -> int:
        # Simplifies Addition/Subtraction Logic
        # When using bit manipulation (XOR, AND, NOT) to simulate arithmetic, 
        # negative numbers (in two’s complement) introduce complexity
        x, y = abs(a), abs(b)

        # Ensure x is the greater absolute value
        # This simplifies logic when handling subtraction (different signs)
        # so the bitwise subtraction logic is safe, predictable, and 
        # avoids Python's quirks with large negative integers.
        if x < y:
            return self.getSum(b, a)

        # Determine the sign of the final result
        # If a is positive, the result should be positive; otherwise, negative
        sign = 1 if a > 0 else -1

        # check if a and b have the same sign (both positive or both negative)
        if a * b >= 0:
            # Case 1: a and b have the same sign (both positive or both negative)
            # Perform addition using bitwise operations
            while y:
                # XOR gives sum without carry
                answer = x ^ y
                # AND followed by left shift gives carry
                carry = (x & y) << 1
                # Repeat the process with new values
                x, y = answer, carry
        else:
            # Case 2: a and b have opposite signs (we're effectively doing subtraction)
            while y:
                # XOR still gives difference without borrow
                answer = x ^ y
                # (~x) & y gives the borrow bits; shift left to apply borrow
                borrow = ((~x) & y) << 1
                x, y = answer, borrow

        # Apply the sign determined earlier
        return x * sign