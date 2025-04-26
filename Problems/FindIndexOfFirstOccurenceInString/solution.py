class Solution:
    def strStr(self, text, pattern):
        if not pattern:
            return -1  # Edge case: empty pattern

        lps = self.compute_lps(pattern)
        matches = []
        j = 0  # index for pattern

        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]

            if text[i] == pattern[j]:
                j += 1

            if j == len(pattern):
                matches.append(i - j + 1)  # match starting index
                j = lps[j - 1]  # keep searching for next match

        
        return matches[0] if len(matches) > 0 else -1

    def compute_lps(self, pattern):
        lps = [0] * len(pattern)
        length = 0

        for i in range(1, len(pattern)):
            while length > 0 and pattern[i] != pattern[length]:
                length = lps[length - 1]

            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length

        return lps
        