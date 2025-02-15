#include <vector>

class Solution 
{
public:

    int LengthOfLIS(vector<int>& Nums) 
    {
        std::vector<int> Table(Nums.size());
        std::fill(Table.begin(), Table.end(), 1);

        for (int i = 1; i < Nums.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (Nums[i] > Nums[j]) {
                    Table[i] = std::max(Table[i], Table[j] + 1);
                }
            }
        }

        return *std::max_element(Table.begin(), Table.end());
    }
};