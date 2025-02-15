#include <iostream>
#include <vector>
#include <algorithm>

class Solution
{
public:
    double findMedianSortedArrays(std::vector<int> &smArr, std::vector<int> &lgArr)
    {
        
        if (lgArr.size() < smArr.size())
        {
            return findMedianSortedArrays(lgArr, smArr);
        }
        
        auto smArrSize = smArr.size();
        auto lgArrSize = lgArr.size();
        int partitionSize = (smArrSize + lgArrSize) / 2;
        
        int smLoIdx = 0;
        int smHiIdx = smArrSize - 1;
        
        int smPartitionIdx;
        int lgPartitionIdx;
        
        while (true) 
        {
            smPartitionIdx = (smLoIdx + smHiIdx) / 2;
            lgPartitionIdx = partitionSize - (smPartitionIdx + 1) - 1;

            auto smLoValue = INT_MIN;
            if (smPartitionIdx >= 0)
            {
                smLoValue = smArr[smPartitionIdx];
            }

            auto smHiValue = INT_MAX;
            if ((smPartitionIdx + 1) < smArrSize)
            {
                smHiValue = smArr[smPartitionIdx + 1];
            }

            auto lgLoValue = INT_MIN;
            if (lgPartitionIdx >= 0)
            {
                lgLoValue = lgArr[lgPartitionIdx];
            }

            auto lgHiValue = INT_MAX;
            if ((lgPartitionIdx + 1) < lgArrSize)
            {
                lgHiValue = lgArr[lgPartitionIdx + 1];
            }

            if ((smLoValue <= lgHiValue) && (lgLoValue <= smHiValue))
            {
                if ((smArrSize + lgArrSize) % 2) {
                    return std::min(smHiValue, lgHiValue);
                }
                return (std::max(smLoValue, lgLoValue) + std::min(smHiValue, lgHiValue)) / 2.0;
            }
            else if (smLoValue > lgHiValue)
            {
                smHiIdx = smPartitionIdx - 1;
            }
            else {
                smLoIdx = smPartitionIdx + 1;  
            }

        }
        
        return 0;
    }
};

int main() {

    std::vector<int> lgArr{0, 1, 1, 3, 6};
    std::vector<int> smArr{4, 5, 6};
    
    Solution runner;

    auto result = runner.findMedianSortedArrays(smArr, lgArr);
    
    std::cout << result << std::endl;

    return 0;
}

