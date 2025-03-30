class Solution(object):
    def count_substrings(self, s):
        # Initialize the total count of palindromic substrings.
        output = 0

        # Iterate through each character in the string.
        # Each character (and the gap between characters) can be a center of a palindrome.
        for i in range(len(s)):
            # Case 1: Odd-length palindromes.
            # Use the same index for left and right pointers (a single center).
            left = right = i
            # Count and add all palindromes expanding from this center.
            output += self.count_palindromes(s, left, right)

            # Case 2: Even-length palindromes.
            # Use the current index and the next index as the center.
            left = i
            right = i + 1
            # Count and add all palindromes expanding from this center.
            output += self.count_palindromes(s, left, right)

        # Return the total count of palindromic substrings.
        return output

    def count_palindromes(self, s, left, right):
        # This helper function counts palindromes using two pointers expanding outwards.
        # Initialize a count for palindromes found from the given center.
        output = 0

        # Expand outwards as long as:
        # - The left pointer is within the string bounds.
        # - The right pointer is within the string bounds.
        # - The characters at the left and right pointers are the same (palindrome condition).
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # We found a palindrome, so increment the count.
            output += 1
            # Move the left pointer one step to the left.
            left -= 1
            # Move the right pointer one step to the right.
            right += 1

        # Return the count of palindromic substrings found from this center.
        return output

solution = Solution()

assert(solution.count_substrings("abc") == 3)
assert(solution.count_substrings("aaa") == 6)

print("PASS")