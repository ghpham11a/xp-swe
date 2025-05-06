class Solution:
    
    def min_remove_to_make_valid(self, s: str) -> str:
        
        # Return empty string if input is None or empty
        if not s:
            return ""

        # Convert the string to a list for in-place modifications
        chars = list(s)

        # Stack to store indices of unmatched '(' characters
        stack = []

        # First pass: remove unmatched ')' by marking them as empty strings
        for index, char in enumerate(chars):
            if char == "(":
                # Record index of '(' to match later
                stack.append(index)
            elif char == ")":
                if stack:
                    # Found a matching '(', remove it from stack
                    stack.pop()
                else:
                    # No matching '(', mark this ')' for removal
                    chars[index] = ""

        # Second pass: remove unmatched '(' by marking their indices as empty
        while stack:
            index = stack.pop()
            chars[index] = ""

        # Reconstruct and return the valid string
        return "".join(chars)
