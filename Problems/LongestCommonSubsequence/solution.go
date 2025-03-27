func longestCommonSubsequence(text1 string, text2 string) int {
    text1Len := len(text1)
    text2Len := len(text2)

    dp := make([][]int, text1Len + 1)
    for i := range dp {
        dp[i] = make([]int, text2Len + 1)
    }

    for text1Idx := 1; text1Idx <= text1Len; text1Idx++ {
        for text2Idx := 1; text2Idx <= text2Len; text2Idx++ {
            if text1[text1Idx - 1] == text2[text2Idx - 1] {
                dp[text1Idx][text2Idx] = 1 + dp[text1Idx - 1][text2Idx - 1]
            } else {
                dp[text1Idx][text2Idx] = max(dp[text1Idx - 1][text2Idx], dp[text1Idx][text2Idx - 1])
            }
        }
    }

    return dp[text1Len][text2Len]
}