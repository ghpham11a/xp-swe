class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, it's impossible for any permutation of s1 to be a substring of s2.
        if len(s1) > len(s2):
            return False

        # Initialize two count arrays of size 26 (one for each lowercase English letter).
        # s1Count holds the frequency counts for each character in s1.
        # s2Count holds the frequency counts for the current window in s2.
        s1Count, s2Count = [0] * 26, [0] * 26

        # Process the first window (of length equal to s1) in both s1 and s2.
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1       # Increment count for the character in s1.
            s2Count[ord(s2[i]) - ord("a")] += 1         # Increment count for the corresponding character in s2.

        # Count how many characters have matching frequency counts between s1Count and s2Count.
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # Use a sliding window in s2; l is the left boundary, and r is the right boundary of the window.
        # Start sliding the window one character at a time, starting from the index len(s1) up to the end of s2.
        l = 0  # Left pointer of the current window in s2.
        for r in range(len(s1), len(s2)):
            # If all 26 characters have matching frequency counts, a permutation is found.
            if matches == 26:
                return True

            # Process the new character entering the window from the right.
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1  # Increment the count for this new character in the window.
            # If after incrementing, the count matches s1Count exactly, we've gained a matching character count.
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If the count went from matching to exceeding, then decrement the match count.
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Process the character that is leaving the window from the left.
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1  # Decrement the count for this character as it is no longer in the window.
            # Check if after removing the character the count matches the count in s1.
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If the count went from matching to being one less, then decrement the match count.
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            # Move the left pointer to slide the window forward.
            l += 1

        # Final check for the last window position.
        return matches == 26