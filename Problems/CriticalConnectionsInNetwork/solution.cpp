#include <vector>
#include <tuple>

class Solution {
public:
    std::vector<vector<int>> CriticalConnections(int N, std::vector<std::vector<int>>& Connections) {
        
        std::vector<std::vector<int>> Graph;
        std::set<std::tuple<int, int>> UniqueEdges;
        std::vector<int> LowLinks(N, -1);
        int Time = 0;

        for (int Node = 0; Node < N; ++Node)
        {
            std::vector<int> Neighbors;
            Graph.push_back(Neighbors);
        }

        for (std::vector<int> Edge : Connections)
        {
            Graph[Edge[0]].push_back(Edge[1]);
            Graph[Edge[1]].push_back(Edge[0]);

            UniqueEdges.insert(std::make_tuple(std::min(Edge[0], Edge[1]), std::max(Edge[0], Edge[1])));
        }

        DFS(Graph, LowLinks, UniqueEdges, 0, Time);

        std::vector<vector<int>> Output;

        for (std::tuple<int, int> UniqueEdge : UniqueEdges) 
        {
            std::vector<int> Edge{std::get<0>(UniqueEdge), std::get<1>(UniqueEdge)};
            Output.push_back(Edge);
        }  

        return Output;

    }

    int DFS(std::vector<std::vector<int>>& Graph, std::vector<int>& LowLinks, std::set<std::tuple<int, int>>& UniqueEdges, int Node, int Time)
    {
        if (LowLinks[Node] > -1)
        {
            return LowLinks[Node];
        }

        LowLinks[Node] = Time;

        int MinTime = Time + 1;

        for (int Neighbor : Graph[Node])
        {
            if (LowLinks[Neighbor] != -1 && LowLinks[Neighbor] == (Time - 1))
            {
                continue;
            }

            int RecursiveRank = DFS(Graph, LowLinks, UniqueEdges, Neighbor, Time + 1);

            if (RecursiveRank <= Time)
            {
                UniqueEdges.erase(std::make_tuple(std::min(Node, Neighbor), std::max(Node, Neighbor)));
            }

            MinTime = std::min(MinTime, RecursiveRank);
        }

        return MinTime;
    }
};