class Solution:

    def compress(self, chars):

        # 'output' will be used as a write pointer (index) in the array,
        # where we store the compressed result.
        # (Note: Initially, there is an unused list assignment which is overwritten by an integer)
        # output = []  <--- (This line is unnecessary since we reassign output to an integer)
        index = 0             # 'index' is the read pointer to traverse the original characters.
        output = 0            # 'output' is the write pointer for placing the compressed characters in the array.

        # Process each group of repeating characters until we have covered the whole array.
        while index < len(chars):

            # Start by assuming the current group has at least one occurrence.
            group_length = 1

            # Check subsequent characters to determine the full length of the group of the current repeated character.
            while (index + group_length < len(chars) and chars[index + group_length] == chars[index]):
                group_length += 1

            # Write the current character (that is starting the group) to the output position.
            chars[output] = chars[index]
            output += 1  # Move the output pointer to the next position.

            # If the group length is more than one, we need to add its count.
            if group_length > 1:
                # Convert the group length to a string so that each digit can be added separately.
                for digit in str(group_length):
                    chars[output] = digit
                    output += 1  # Increment the output pointer for each digit inserted.

            # Move the read pointer ('index') to the next group (skip all characters that were in the current group).
            index += group_length

        # After processing, 'output' holds the new length of the compressed list.
        return output

solution = Solution()

test_input = ["a","a","b","b","c","c","c"]
assert(solution.compress(test_input) == 6)


print("PASS")