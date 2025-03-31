class Solution:
    def calculate(self, s: str) -> int:
        # Initialize a pointer to iterate over the string.
        index = 0

        # 'curr' is used to build the current number from consecutive digits.
        curr = 0

        # 'prev' holds the last computed value from the previous operation.
        # This is important for handling '*' and '/' operations due to operator precedence.
        prev = 0

        # 'output' accumulates the result of the expression.
        output = 0

        # Define the set of valid operators.
        OPERATIONS = { "+", "-", "*", "/" }

        # Initialize the current operation to '+' (default operation for the first number).
        curr_operation = "+"

        # Process the string one character at a time.
        while index < len(s):
            curr_char = s[index]

            # If the character is a digit, build the complete number (which may have multiple digits).
            if curr_char.isdigit():
                # Continue forming the number until a non-digit is encountered.
                while index < len(s) and s[index].isdigit():
                    curr = curr * 10 + int(s[index])
                    index += 1

                # After the inner loop, index is at the first non-digit character.
                # Decrement index by 1 because the outer loop will increment it again.
                index -= 1

                # Process the current number based on the last operator seen.
                if curr_operation == "+":
                    # For addition, add the current number to the output.
                    output += curr
                    # Update prev to the current number for potential future '*' or '/' operations.
                    prev = curr
                elif curr_operation == "-":
                    # For subtraction, subtract the current number from the output.
                    output -= curr
                    # Store the negative of the current number in prev.
                    prev = -curr
                elif curr_operation == "*":
                    # For multiplication, adjust the output by removing the last added number (prev)
                    # and adding the result of multiplying prev with the current number.
                    output -= prev
                    output += (prev * curr)
                    # Update prev to be the multiplication result.
                    prev = prev * curr
                elif curr_operation == "/":
                    # For division, first remove the last value (prev) from output.
                    output -= prev
                    # Divide prev by the current number and truncate the result toward zero.
                    # The int() conversion truncates the result.
                    output += int(prev / curr)
                    # Update prev with the truncated division result.
                    prev = int(prev / curr)

                # Reset the current number after processing.
                curr = 0

            # If the current character is an operator, update the current operation.
            if curr_char in OPERATIONS:
                curr_operation = curr_char

            # If the character is a space, do nothing.
            if curr_char == " ":
                pass

            # Move to the next character in the string.
            index += 1

        # Return the final computed result of the expression.
        return output


solution = Solution()

assert(solution.calculate("3+2*2") == 7)

print("PASS")