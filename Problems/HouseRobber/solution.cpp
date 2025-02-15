class Solution {
public:
    int rob(vector<int>& nums) {
        
        if (nums.empty())
        {
            return 0;
        }

        if (nums.size() == 1)
        {
            return nums[0];
        }

        if (nums.size() == 2)
        {
            return std::max(nums[0], nums[1]);
        }

        std::vector<int> DP(nums.size(), 0);

        DP[0] = nums[0];
        DP[1] = std::max(nums[0], nums[1]);

        for (int HomeIndex = 2; HomeIndex < nums.size(); ++HomeIndex)
        {
            DP[HomeIndex] = std::max(nums[HomeIndex] + DP[HomeIndex - 2], DP[HomeIndex - 1]);
        }

        return DP.back();
    }
};