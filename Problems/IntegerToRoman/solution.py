class Solution:
    def int_to_roman(self, num):
        # List of tuples mapping values to their Roman numeral symbols.
        # Ordered from largest to smallest to handle conversion properly.
        digits = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        # Initialize an empty list to build the Roman numeral string piece by piece.
        output = []

        # Iterate over each (value, symbol) pair in the digits list
        for value, symbol in digits:
            # If the number becomes 0, we can stop early.
            if num == 0:
                break

            # Use divmod to get:
            # - count: how many times 'value' fits into 'num'
            # - num: the remainder after extracting 'count' * 'value'
            count, num = divmod(num, value)

            # Append the symbol 'count' number of times to the output
            # (e.g., if count == 3 and symbol == 'C', append 'CCC')
            output.append(symbol * count)

        # Join all parts together into the final Roman numeral string and return it.
        return "".join(output)
    
solution = Solution()

assert(solution.int_to_roman(1994) == "MCMXCIV")

print("PASS")