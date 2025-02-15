class Solution:
    def calculate(self, s: str) -> int:
        
        index = 0

        curr = 0
        prev = 0
        output = 0

        OPERATIONS = { "+", "-", "*", "/" }

        curr_operation = "+"

        while index < len(s):
            curr_char = s[index]

            if curr_char.isdigit():
                while index < len(s) and s[index].isdigit():
                    curr = curr * 10 + int(s[index])
                    index += 1
                
                index -= 1

                if curr_operation == "+":
                    output += curr
                    prev = curr
                elif curr_operation == "-":
                    output -= curr
                    prev = -curr
                elif curr_operation == "*":
                    output -= prev
                    output += (prev * curr)
                    prev = curr * prev
                elif curr_operation == "/":
                    output -= prev 
                    output += int(prev / curr)
                    prev = int(prev / curr)

                curr = 0

            if curr_char in OPERATIONS:
                curr_operation = curr_char

            if curr_char == " ":
                pass

            index += 1

        return output

solution = Solution()

assert(solution.calculate("3+2*2") == 7)

print("PASS")