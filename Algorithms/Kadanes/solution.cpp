#include <limits>
#include <vector>

int Kadanes(std::vector<int>& Nums)
{
    int BestSum = std::numeric_limits<int>::max();
    int CurrentSum = 0;

    for (int Num : Nums)
    {
        CurrentSum = std::max(CurrentSum, CurrentSum + Num);
        BestSum = std::max(BestSum, CurrentSum);
    }

    return BestSum;
}