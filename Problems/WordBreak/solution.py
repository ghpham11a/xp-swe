from typing import List

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        len_s = len(s)

        # dp[i] represents whether the substring s[i:] can be segmented into words from wordDict
        dp = [False] * (len_s + 1)
        dp[len_s] = True  # Base case: empty string is segmentable

        # Iterate backwards from the end of the string to the beginning
        for i in range(len_s - 1, -1, -1):
            # Try every word in the dictionary
            for w in wordDict:
                len_w = len(w)
                # Check if the word fits in the current position and matches the substring
                if (i + len_w) <= len_s and s[i:i + len_w] == w:
                    # If s[i:i+len(w)] is a word and the remainder s[i+len(w):] is segmentable
                    dp[i] = dp[i + len_w]
                if dp[i]:
                    # Early break: no need to check other words if we already found a valid break
                    break

        # The result is whether the full string s[0:] can be segmented
        return dp[0]

solution = Solution()

assert(solution.word_break("leetcode", ["leet","code"]) == True)

print("PASS")