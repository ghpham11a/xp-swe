class Solution:
    def length_of_longest_substring(self, s):
        # Set to keep track of characters in the current window to detect duplicates.
        chars_seen = set()
        
        # Initialize the left pointer of the sliding window.
        left = 0
        # Variable to store the maximum length of substring without repeating characters.
        output = 0

        # Iterate through the string with the right pointer.
        for right in range(len(s)):
            # If the current character is already in the set, it means we found a duplicate.
            # Shrink the window from the left until the duplicate is removed.
            while s[right] in chars_seen:
                # Remove the character at the left pointer from the set.
                chars_seen.remove(s[left])
                # Move the left pointer one step to the right.
                left += 1
            
            # Add the current character to the set, as it's now part of the current window.
            chars_seen.add(s[right])
            
            # Update the output with the length of the current window if it's larger than previous maximum.
            # The current window length is (right - left + 1).
            output = max(output, right - left + 1)
        
        # Return the maximum length found.
        return output