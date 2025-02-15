class Solution 
{
public:

    std::vector<std::vector<int>> Subsets(std::vector<int>& Nums) 
    {
        std::vector<std::vector<int>> Output;
        std::vector<int> InitSubOutput;
        Backtrack(Nums, Output, InitSubOutput, 0);
        return Output;
    }

    void Backtrack(std::vector<int>& Nums, std::vector<std::vector<int>>& Output, std::vector<int>& SubOutput, int Index)
    {
        if (Index >= Nums.size())
        {
            std::vector<int> SubOutputCopy(SubOutput);
            Output.push_back(SubOutputCopy);
            return;
        }

        SubOutput.push_back(Nums[Index]);
        Backtrack(Nums, Output, SubOutput, Index + 1);

        SubOutput.pop_back();
        Backtrack(Nums, Output, SubOutput, Index + 1);
    }
};