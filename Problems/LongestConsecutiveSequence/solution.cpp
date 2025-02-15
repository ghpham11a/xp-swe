#include <vector>
#include <set>
#include <algorithm>
#include <cassert>

class Solution
{
    int LongestConsecutive(std::vector<int>& Nums)
    {
        int LongestStreak = 0;
        std::set<int> NumSet(Nums.begin(), Nums.end());

        for (int Num : NumSet)
        {
            if (!NumSet.contains(Num - 1))
            {
                int CurrentNum = Num;
                int CurrentStreak = 1;
                
                while (NumSet.contains(CurrentNum + 1))
                {
                    CurrentNum += 1;
                    CurrentStreak += 1;
                }

                LongestStreak = std::max(LongestStreak, CurrentStreak);
            }
        }

        return LongestStreak;
    }
};

int main()
{
    Solution Runner;
    std::vector<int> TestInput{100,4,200,1,3,2};
    assert(Runner.LongestConsecutive(TestInput) == 4);

    std::cout << "PASS";

    return 0;
}