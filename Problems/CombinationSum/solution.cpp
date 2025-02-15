#include <vector>

class Solution 
{    
public:

    std::vector<std::vector<int>> SubOutputSum(std::vector<int>& Candidates, int Target) 
    {
        std::vector<std::vector<int>> Output;
        std::vector<int> InitSubOutput;
        Backtrack(Candidates, Target, InitSubOutput, 0, Output);
        return Output;
    }

    void Backtrack(std::vector<int>& Candidates, int Target, std::vector<int>& SubOutput, int StartIndex, std::vector<std::vector<int>>& Output) 
    {

        if (Target == 0) 
        {
            std::vector<int> SubOutputCopy(SubOutput);
            Output.push_back(SubOutputCopy);
            return;
        }

        if (Target < 0) 
        {
            return;
        }

        for (int i = StartIndex; i < Candidates.size(); ++i) 
        {
            SubOutput.push_back(Candidates[i]);
            Backtrack(Candidates, Target - Candidates[i], SubOutput, i, Output);
            SubOutput.pop_back();
        }
    }
};