#include <vector>
#include <unordered_map>
#include <tuple>
#include <set>

class Solution 
{
public:
    int NetworkDelayTime(vector<vector<int>>& Times, int N, int K) {
        
        std::unordered_map<int, std::vector<std::tuple<int, int>>> Graph;

        for (int Node = 1; Node < N + 1; ++Node)
        {
            std::vector<std::tuple<int, int>> Neighbor;
            Graph[Node] = Neighbor;
        }

        for (std::vector<int> Edge : Times)
        {
            Graph[Edge[0]].push_back(std::make_tuple(Edge[1], Edge[2]));
        }

        std::priority_queue<
            std::tuple<int, int>,
            std::vector<std::tuple<int, int>>,
            std::greater<std::tuple<int, int>>
        > PQ;
        std::set<int> Visited;
        int Output = 0;

        PQ.push(std::make_tuple(0, K));

        while (!PQ.empty())
        {
            std::tuple<int, int> Top = PQ.top();
            int SrcWeight = std::get<0>(Top);
            int Src = std::get<1>(Top);
            PQ.pop();

            if (Visited.contains(Src))
            {
                continue;
            }

            Visited.insert(Src);
            Output = std::max(Output, SrcWeight);

            for (std::tuple<int, int> Edge : Graph[Src])
            {
                int Dst = std::get<0>(Edge);
                int DstWeight = std::get<1>(Edge);
                if (!Visited.contains(Dst))
                {
                    PQ.push(std::make_tuple(SrcWeight + DstWeight, Dst));
                }
            }

        }

        if (Visited.size() == N)
        {
            return Output;
        }
        else
        {
            return -1;
        }
    }
};