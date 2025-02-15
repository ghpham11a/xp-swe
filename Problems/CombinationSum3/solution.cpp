class Solution {
public:

    std::vector<std::vector<int>> combinationSum3(int k, int n) {
        std::vector<int> candidates { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        std::vector<std::vector<int>> output;
        std::vector<int> startCombination;
        backtrack(candidates, n, k, startCombination, 0, output);
        return output;
    }

    void backtrack(std::vector<int>& candidates, int target, int limit, std::vector<int>& combination, int startIndex, std::vector<std::vector<int>>& output) {

        if (target == 0 && combination.size() == limit) {
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
            backtrack(candidates, target - candidates[i], limit, combination, i + 1, output);
            combination.pop_back();
        }

    }
};