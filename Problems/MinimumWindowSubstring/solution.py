class Solution:
    def min_window(self, s, t):
        # Edge case: if t is empty, return an empty string
        if t == "":
            return ""

        # Dictionaries to keep track of character counts
        countT, window = {}, {}

        # Build the countT dictionary to count characters in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Variables to track how many characters meet the requirement
        have, need = 0, len(countT)

        # Variables to store the best (smallest) window's bounds and length
        output, output_len = [-1, -1], float("inf")

        # Left pointer of the window
        l = 0

        # Expand the right pointer of the window
        for r in range(len(s)):
            c = s[r]
            # Add character to the window count
            window[c] = 1 + window.get(c, 0)

            # If the current character meets the required count, increment 'have'
            if c in countT and window[c] == countT[c]:
                have += 1

            # When the window satisfies all character counts
            while have == need:
                # Update the best window if this one is smaller
                if (r - l + 1) < output_len:
                    output = [l, r]
                    output_len = (r - l + 1)

                # Shrink the window from the left
                window[s[l]] -= 1
                # If removing this character means we no longer satisfy t's requirement
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # Move left pointer to shrink the window
                l += 1

        # After processing, extract the substring from the best window found
        l, r = output
        return s[l:r + 1] if output_len != float("inf") else ""
    
solution = Solution()

assert(solution.min_window("ADOBECODEBANC", "ABC") == "BANC")
    
print("PASS")