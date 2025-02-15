class Solution {
public:

    std::vector<std::vector<int>> combinationSum2(std::vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        std::vector<std::vector<int>> output;
        std::vector<int> startCombination;
        backtrack(candidates, target, startCombination, 0, output);
        return output;
    }

    void backtrack(std::vector<int>& candidates, int target, std::vector<int>& combination, int startIndex, std::vector<std::vector<int>>& output) {

        if (target == 0) {
            std::vector<int> combinationCopy(combination);
            output.push_back(combinationCopy);
            return;
        }

        if (target < 0) {
            return;
        }

        for (int i = startIndex; i < candidates.size(); ++i) {

            if (i > startIndex && candidates[i] == candidates[i - 1]) {
                continue;
            }

            combination.push_back(candidates[i]);
            backtrack(candidates, target - candidates[i], combination, i + 1, output);
            combination.pop_back();
        }

    }
};