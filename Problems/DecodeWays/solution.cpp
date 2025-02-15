#include <vector>

class Solution 
{
public:
    int NumDecodings(string S) 
    {

        if (S[0] == '0')
        {
            return 0;
        }

        std::vector<int> Table(S.size() + 1);
        fill(Table.begin(), Table.end(), 0);
        
        Table[0] = 1;
        Table[1] = 1;

        for (int i = 2; i < S.size() + 1; ++i)
        {
            if (S[i - 1] > '0')
            {
                Table[i] = Table[i - 1];
            }

            if (S[i - 2] == '1' || (S[i - 2] == '2' && S[i - 1] < '7'))
            {
                Table[i] += Table[i - 2];
            }
        } 

        return Table.back();
    }
};