class Solution:
    
    def calculate(self, s: str) -> int:

        stack = []
        curr = 0
        previous_operator = "+"
        s += "@"
        
        for c in s:

            if c == " ":
                continue

            if c.isdigit():
                curr = curr * 10 + int(c)

            elif c == "(":
                stack.append(previous_operator)
                previous_operator = "+"
            else:

                if previous_operator == "*":
                    stack.append(stack.pop() * curr)

                if previous_operator == "/":
                    stack.append(int(stack.pop() / curr))

                if previous_operator == "+":
                    stack.append(curr)

                if previous_operator == "-":
                    stack.append(-curr)
                
                curr = 0
                previous_operator = c
                if c == ")":
                    while type(stack[-1]) == int:
                        curr += stack.pop()
                    previous_operator = stack.pop()

        return sum(stack)

solution = Solution()

assert(solution.calculate("2*(5+5*2)/3+(6/2+8)") == 21)

print("PASS")