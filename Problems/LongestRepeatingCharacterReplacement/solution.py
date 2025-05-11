class Solution:

    def characterReplacement(self, s, k):
        # Dictionary to keep count of character frequencies in the current window.
        count = {}
        # Variable to keep track of the maximum length (result) found so far.
        output = 0

        # Initialize the left pointer of the sliding window.
        left = 0
        # 'maxf' will hold the count of the most frequent character in the current window.
        maxf = 0
        
        # Iterate over each character in the string using its index as the right pointer.
        for right in range(len(s)):
            # Increase the count for the current character by 1.
            # If the character isn't in the dictionary yet, use 0 as the default.
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Update maxf to be the maximum frequency we've seen in the current window so far.
            # This is essential because it indicates how many characters are already the same.
            maxf = max(maxf, count[s[right]])
            
            # Check if the current window size minus the count of the most frequent character
            # exceeds k. This is the number of characters that need to be replaced
            # to make the entire window the same letter.
            while (right - left + 1) - maxf > k:
                # If more than k characters need to be replaced, shrink the window from the left.
                count[s[left]] -= 1
                left += 1  # Move the left pointer rightward.
            
            # Update the output with the larger window found so far.
            # The window [left, right] now represents a valid substring where at most k changes are needed.
            output = max(output, right - left + 1)
        
        # Return the length of the longest valid substring found.
        return output