class Solution:
    
    def calculate(self, s: str) -> int:
        # Initialize a stack to store intermediate results and operators.
        # This stack will help handle nested expressions and operator precedence.
        stack = []
        
        # 'curr' accumulates the current number being read from the string.
        curr = 0
        
        # 'previous_operator' stores the last operator seen.
        # Initialized to '+' so that the first number is treated as positive.
        previous_operator = "+"
        
        # Append a sentinel character (here "@") to force processing of the last number.
        s += "@"
        
        # Iterate over each character in the modified string.
        for c in s:
            # Skip any spaces in the expression.
            if c == " ":
                continue

            # If the current character is a digit, update 'curr' by appending the digit.
            if c.isdigit():
                # Multiply current value by 10 and add the new digit (handles multi-digit numbers).
                curr = curr * 10 + int(c)
            
            # If the character is an open parenthesis '(',
            # we need to start a new sub-expression.
            elif c == "(":
                # Push the current operator onto the stack.
                # This operator is saved to apply once the sub-expression inside the parentheses is evaluated.
                stack.append(previous_operator)
                # Reset the operator to '+' for the new sub-expression.
                previous_operator = "+"
            
            # For any other character (operators, closing parenthesis, or the sentinel),
            # we process the current number and the previous operator.
            else:
                # Based on the previous operator, perform the corresponding calculation:
                if previous_operator == "*":
                    # For multiplication, pop the last number from the stack,
                    # multiply it with 'curr', and push the product back onto the stack.
                    stack.append(stack.pop() * curr)
                if previous_operator == "/":
                    # For division, pop the last number from the stack,
                    # divide it by 'curr' (with truncation toward zero), and push the result.
                    stack.append(int(stack.pop() / curr))
                if previous_operator == "+":
                    # For addition, simply push the current number onto the stack.
                    stack.append(curr)
                if previous_operator == "-":
                    # For subtraction, push the negative of the current number onto the stack.
                    stack.append(-curr)
                
                # Reset 'curr' to zero to start processing the next number.
                curr = 0
                
                # Update the 'previous_operator' to the current character.
                previous_operator = c
                
                # If the current character is a closing parenthesis ')',
                # it means the end of a sub-expression.
                if c == ")":
                    # 'curr' will accumulate the sum of values within the parentheses.
                    while type(stack[-1]) == int:
                        # Pop and add each number from the stack that belongs to the sub-expression.
                        curr += stack.pop()
                    # Once we exit the loop, the next element in the stack is the operator
                    # that was saved before the matching '('.
                    previous_operator = stack.pop()

        # Finally, sum up all numbers in the stack to get the final result.
        return sum(stack)


solution = Solution()

assert(solution.calculate("2*(5+5*2)/3+(6/2+8)") == 21)

print("PASS")