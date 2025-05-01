class Solution:

    def remove_k_digits(self, num, k):
        # Initialize an empty stack to keep track of digits
        stack = []

        # Iterate over each digit in the number string
        for c in num:
            # While we still need to remove digits (k > 0),
            # and the stack is not empty,
            # and the last digit in the stack is greater than the current digit,
            # pop the stack to remove a larger digit and make the number smaller
            while k > 0 and stack and stack[-1] > c:
                k -= 1          # Decrement k because we've removed a digit
                stack.pop()     # Remove the top (larger) digit

            # Add the current digit to the stack
            stack.append(c)

        # If k digits haven't been removed yet (e.g. number is increasing),
        # remove from the end of the stack (least significant digits)
        stack = stack[:len(stack) - k]

        # Join the digits and remove leading zeros, return "0" if empty
        output = "".join(stack).lstrip('0') or "0"

        return output

solution = Solution()

assert(solution.remove_k_digits("1432219", 3) == "1219")

print("PASS")