class Solution:
    def int_to_roman(self, num):
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]

        output = []

        for value, symbol in digits:

            if num == 0:
                break

            count, num = divmod(num, value)
            output.append(symbol * count)

        return "".join(output)
    
solution = Solution()

assert(solution.int_to_roman(1994) == "MCMXCIV")

print("PASS")