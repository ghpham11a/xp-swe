class Solution:

    def calculate(self, s):
        # Initialize an empty stack to save previous results and signs when encountering '('.
        stack = []
        
        # 'operand' holds the current number being built from consecutive digits.
        operand = 0
        
        # 'output' holds the cumulative result so far.
        output = 0  # This is the ongoing result of the expression.
        
        # 'sign' represents the current sign for the operand: 1 for positive, -1 for negative.
        sign = 1  # Initially set to positive.
        
        # Loop over every character in the string expression.
        for ch in s:
            if ch.isdigit():
                # If the character is a digit, build the operand.
                # Multiply the previous operand by 10 and add the new digit.
                operand = (operand * 10) + int(ch)
            
            elif ch == '+':
                # When encountering a plus, finish the current operand.
                # Multiply the operand by the current sign and add it to the output.
                output += sign * operand
                
                # Set sign to positive for the next operand.
                sign = 1
                
                # Reset operand for the next number.
                operand = 0
            
            elif ch == '-':
                # When encountering a minus, finish the current operand.
                output += sign * operand
                
                # Set sign to negative for the next operand.
                sign = -1
                
                # Reset operand.
                operand = 0
            
            elif ch == '(':
                # When an open parenthesis is found, push the current output and sign
                # onto the stack. This saves the current context.
                stack.append(output)  # Save the current result.
                stack.append(sign)    # Save the current sign.
                
                # Reset output and sign for the new sub-expression inside the parentheses.
                output = 0
                sign = 1  # Reset sign to positive as new sub-expression starts.
                # 'operand' remains 0 as well.
            
            elif ch == ')':
                # When a closing parenthesis is reached, complete the sub-expression:
                # Add the current operand to the output using the current sign.
                output += sign * operand
                
                # The sign before the parenthesis is the last element on the stack.
                # Multiply the current output (result of the sub-expression) by that sign.
                output *= stack.pop()  # Pop the sign saved earlier.
                
                # Next, add the output before the parenthesis (saved earlier) to the current result.
                output += stack.pop()  # Pop the previous result.
                
                # Reset operand for the next number.
                operand = 0
        
        # After processing all characters, there might be an operand left.
        # Multiply it by the last sign and add to the final output.
        output += (sign * operand)
        
        # Return the final evaluated result.
        return output

solution = Solution()

assert(solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23)

print("PASS")