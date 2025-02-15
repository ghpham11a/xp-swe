class Solution:
    
    def min_remove_to_make_valid(self, s):
        
        # error checking
        if not s:
            return ""

        # split string and create stack
        stack = []
        chars = list(s)

        # loop through chars and modify parenthesis as needed
        for index, char in enumerate(chars):
            if char == "(":
                stack.append(index)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    chars[index] = ""

        # check if there are excess open parens, and remove them
        while stack:
            index = stack.pop()
            chars[index] = ""

        # return joined answer
        return "".join(chars)
