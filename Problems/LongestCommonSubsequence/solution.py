class Solution:

    def longest_common_subsequence(self, text_1: str, text_2: str) -> int:
        text1_len = len(text_1)
        text2_len = len(text_2)

        dp = [[0] * (text2_len + 1) for _ in range(text1_len + 1)]

        for text1_idx in range(1, text1_len + 1):
            for text2_idx in range(1, text2_len + 1):
                if text_1[text1_idx - 1] == text_2[text2_idx - 1]:
                    dp[text1_idx][text2_idx] = 1 + dp[text1_idx - 1][text2_idx - 1]
                else:
                    dp[text1_idx][text2_idx] = max(dp[text1_idx - 1][text2_idx], dp[text1_idx][text2_idx - 1])

        return dp[text1_len][text2_len]

solution = Solution()

assert(solution.longest_common_subsequence("abcde", "ace") == 3)

print("PASS")