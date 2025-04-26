class Solution:
    def isAnagram(self, s, t):

        # If the lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Initialize a table to count occurrences of each character (assuming lowercase English letters)
        table = [0] * 26

        # Count each character in string s
        for char in s:
            table[ord(char) - ord('a')] += 1

        # Subtract the count for each character in string t
        for char in t:
            table[ord(char) - ord('a')] -= 1
            # If any count goes negative, t has an extra character not matched in s
            if table[ord(char) - ord('a')] < 0:
                return False

        # If all counts are zero, it's an anagram
        return True