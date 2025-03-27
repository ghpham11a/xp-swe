#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int longestCommonSubsequence(string text1, string text2) {
    int text1Len = text1.size();
    int text2Len = text2.size();

    vector<vector<int>> dp(text1Len + 1, vector<int>(text2Len + 1, 0));

    for (int text1Idx = 1; text1Idx <= text1Len; text1Idx++)
    {
        for (int text2Idx = 1; text2Idx <= text2Len; text2Idx++)
        {
            if (text1[text1Idx - 1] == text2[text2Idx - 1])
            {
                dp[text1Idx][text2Idx] = 1 + dp[text1Idx - 1][text2Idx - 1];
            }
            else
            {
                dp[text1Idx][text2Idx] = max(dp[text1Idx - 1][text2Idx], dp[text1Idx][text2Idx - 1]);
            }
        }
    }

    return dp[text1Len][text2Len];
}

int main() {
    // Test the function
    string text1 = "abcde";
    string text2 = "ace";

    int result = longestCommonSubsequence(text1, text2);
    if (result == 3) {
        cout << "PASS" << endl;
    } else {
        cout << "FAIL" << endl;
    }

    return 0;
}