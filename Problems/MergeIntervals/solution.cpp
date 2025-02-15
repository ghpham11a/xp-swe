#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> Merge(std::vector<std::vector<int>>& Intervals) {

        std::sort(Intervals.begin(), Intervals.end(), 
            [](const std::vector<int>& a, const std::vector<int>& b) 
            {
                return a[0] < b[0];
            }
        );
        
        std::vector<std::vector<int>> Output;

        Output.push_back(Intervals[0]);

        for (int Index = 1; Index < Intervals.size(); ++Index)
        {
            int Start = Intervals[Index][0];
            int End = Intervals[Index][1];

            int LastEnd = Output.back()[1];

            if (Start <= LastEnd)
            {
                Output.back()[1] = std::max(End, LastEnd);
            }
            else
            {
                std::vector<int> Interval{Start, End};
                Output.push_back(Interval);
            }
        }

        return Output;
    }
};