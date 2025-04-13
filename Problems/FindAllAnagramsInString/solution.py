class Solution:
    def findAnagrams(self, s, p):
        # If p is longer than s, there is no substring of s that can be an anagram of p.
        if len(p) > len(s):
            return []  

        # Initialize dictionaries to count character frequencies in 'p' and the current window in 's'.
        p_count, s_count = {}, {}

        # Build the frequency dictionaries for 'p' and for the first window of 's' with length equal to len(p).
        for i in range(len(p)):
            p_count[p[i]] = 1 + p_count.get(p[i], 0)  # Count frequency of each char in p.
            s_count[s[i]] = 1 + s_count.get(s[i], 0)  # Count frequency for the first len(p) characters in s.

        # Initialize the output list.
        # If the frequency count of the first window in 's' matches 'p_count', then index 0 is a valid starting index.
        output = [0] if s_count == p_count else []

        # 'left' pointer to mark the beginning of the sliding window.
        left = 0

        # Iterate over s starting from index len(p) to the end.
        for right in range(len(p), len(s)):
            # Add the current character (entering the window) to the frequency count.
            s_count[s[right]] = 1 + s_count.get(s[right], 0)

            # Decrease the frequency of the character at the left side of the window, since it will be removed.
            s_count[s[left]] -= 1

            # If the frequency becomes zero, remove it from the dictionary to keep the dictionary clean.
            if s_count[s[left]] == 0:
                s_count.pop(s[left])
            
            # Move the left pointer to the right, effectively sliding the window forward.
            left += 1

            # If the current window's frequency dictionary matches that of 'p', record the start index.
            if s_count == p_count:
                output.append(left)

        # Return the list of starting indices where the anagrams of p begin in s.
        return output
