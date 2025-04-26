class Solution:
    def is_subsequence(self, s, t):
        # Initialize two pointers: 
        # i points to the current character in s
        # j points to the current character in t
        i, j = 0, 0

        # Loop through both strings until one of them is fully traversed
        while i < len(s) and j < len(t):
            # If the characters match, move the pointer in s
            if s[i] == t[j]:
                i += 1
            # Always move the pointer in t
            j += 1

        # If we have gone through all characters in s, it means s is a subsequence of t
        return i == len(s)