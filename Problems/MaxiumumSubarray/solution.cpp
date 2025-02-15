#include <limit>
#include <algorithm>
#include <vector>

class Solution {
public:
    int MaxSubArray(vector<int>& Nums) 
    {

        int BestSum = std::numeric_limits<int>::min();
        int CurrentSum = 0;

        for (int Num : Nums)
        {
            CurrentSum = std::max(Num, CurrentSum + Num);
            BestSum = std::max(BestSum, CurrentSum);
        }

        return BestSum;
    }
};

int main()
{

    Solution Runner;

    std::vector<int> TestInput{-2,1,-3,4,-1,2,1,-5,4};
    assert(Runner.MaxSubArray(TestInput) == 6);

    std::cout << "PASS";

    return 0;
}