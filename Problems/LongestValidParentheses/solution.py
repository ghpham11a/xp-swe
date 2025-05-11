class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize counters for the number of '(' (left), ')' (right), and the maximum valid length found so far
        left, right, maxlength = 0, 0, 0

        # First pass: left to right
        for i in range(len(s)):
            if s[i] == "(":        # Increment left counter for open parenthesis
                left += 1
            else:                  # Increment right counter for close parenthesis
                right += 1

            if left == right:      # If both counters are equal, it's a valid substring
                maxlength = max(maxlength, 2 * right)
            elif right > left:     # If ')' are more than '(', reset counters
                left = right = 0

        # Reset counters for second pass
        left = right = 0

        # Second pass: right to left (handles cases like "(()")
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":        # Increment left counter for open parenthesis
                left += 1
            else:                  # Increment right counter for close parenthesis
                right += 1

            if left == right:      # If both counters are equal, it's a valid substring
                maxlength = max(maxlength, 2 * left)
            elif left > right:     # If '(' are more than ')', reset counters
                left = right = 0

        # Return the length of the longest valid parentheses substring found
        return maxlength