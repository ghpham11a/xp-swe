#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> permute(std::vector<int>& nums) 
    {
        std::vector<std::vector<int>> output;
        std::vector<int> initSubOutput;
        backtrack(nums, initSubOutput, output);
        return output;
    }

    void backtrack(std::vector<int>& nums, std::vector<int>& subOutput, std::vector<std::vector<int>>& output) 
    {
        if (subOutput.size() == nums.size()) 
        {
            std::vector<int> subOutputCopy(subOutput);
            output.push_back(subOutputCopy);
            return;
        }

        for (auto num : nums) 
        {
            // Check if num is not in subOutput
            if (std::find(subOutput.begin(), subOutput.end(), num) == subOutput.end()) 
            {
                subOutput.push_back(num);
                backtrack(nums, subOutput, output);
                subOutput.pop_back();
            }
        }

    }
};