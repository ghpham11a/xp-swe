#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> Insert(std::vector<std::vector<int>>& Intervals, std::vector<int>& NewInterval) {

        std::vector<std::vector<int>> Output;

        for (int Index = 0; Index < Intervals.size(); ++Index)
        {
            if (NewInterval[1] < Intervals[Index][0])
            {
                Output.push_back(NewInterval);
                Output.insert(Output.end(), Intervals.begin() + Index, Intervals.end());
                return Output;
            }
            else if (NewInterval[0] > Intervals[Index][1])
            {

                Output.push_back(Intervals[Index]);
            }   
            else
            {
                NewInterval[0] = std::min(NewInterval[0], Intervals[Index][0]); 
                NewInterval[1] = std::max(NewInterval[1], Intervals[Index][1]); 
            }
        }

        Output.push_back(NewInterval);

        return Output;
    }
};