#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& Numbers, int Target) {
        
        int Left = 0;
        int Right = Numbers.size() - 1;

        std::vector<int> Output;

        while (Left < Right) 
        {
            int TwoSum = Numbers[Left] + Numbers[Right];

            if (TwoSum > Target)
            {
                Right -= 1;
            }
            else if (TwoSum < Target)
            {
                Left += 1;
            }
            else
            {
                Output.push_back(Left + 1);
                Output.push_back(Right + 1);
                break;
            }
        }
        return Output;
    }
};