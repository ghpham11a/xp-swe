class Solution:

    def compress(self, chars):

        output = []

        index = 0
        output = 0

        while index < len(chars):

            group_length = 1
            while (index + group_length < len(chars) and chars[index + group_length] == chars[index]):
                group_length += 1

            chars[output] = chars[index]
            output += 1

            if group_length > 1:

                for digit in str(group_length):
                    chars[output] = digit
                    output += 1

            index += group_length

        return output

solution = Solution()

test_input = ["a","a","b","b","c","c","c"]
assert(solution.compress(test_input) == 6)


print("PASS")