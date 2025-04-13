class Solution:
    def minFlips(self, s):
        # Get the length of the input string.
        n = len(s)
        
        # Duplicate the input string by concatenating it with itself.
        # This doubling simulates all possible rotations.
        # Every rotation of the string can be seen as a contiguous substring 
        # (of length n) in the string s+s.
        s = s + s
        
        # Initialize two empty strings that will be used to store two possible alternating patterns.
        # One pattern (alt1) will represent an alternating sequence starting with '1'
        # and the other (alt2) will start with '0'.
        alt1, alt2 = "", ""
        
        # Build the two target alternating patterns for the doubled string length.
        for i in range(len(s)):
            # For alt1: if the index is even (i % 2 == 0), append '1', otherwise append '0'.
            # For alt2: the opposite; for even indices append '0', for odd indices append '1'.
            alt1 += "0" if i % 2 else "1"
            alt2 += "1" if i % 2 else "0"
        
        # Initialize the result with a large number (maximum possible flips),
        # here we use the length of s (which is 2*n) as an upper bound.
        res = len(s)
        
        # These counters will track the number of mismatches (flips needed) in the current window:
        # diff1 counts differences compared to alt1 and diff2 compared to alt2.
        diff1, diff2 = 0, 0
        
        # Initialize a left pointer for the sliding window.
        l = 0
        
        # Use a sliding window to iterate through the doubled string (from index 0 to len(s)-1).
        for r in range(len(s)):
            # If the character at the current right pointer does not match the corresponding character in alt1,
            # increment diff1 because this indicates a necessary flip.
            if s[r] != alt1[r]:
                diff1 += 1
            # Similarly update diff2 based on the pattern alt2.
            if s[r] != alt2[r]:
                diff2 += 1

            # If the current window size exceeds n, it means we have more characters than the original string,
            # so we need to shrink the window from the left.
            if (r - l + 1) > n:
                # Check if the character at the left pointer was a mismatch with alt1.
                # If it was, we reduce diff1 as this character is no longer in the window.
                if s[l] != alt1[l]:
                    diff1 -= 1
                # Similarly, adjust diff2 if needed.
                if s[l] != alt2[l]:
                    diff2 -= 1
                
                # Move the left pointer forward, effectively reducing the window size by one.
                l += 1

            # When the window size is exactly n,
            # we are looking at a valid rotation of the original string.
            if (r - l + 1) == n:
                # Update the result with the minimum mismatch count seen so far between the two patterns.
                res = min(res, diff1, diff2)

        # Return the minimum number of type-2 (flip) operations required
        # to transform some rotation of s into an alternating string.
        return res