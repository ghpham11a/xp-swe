#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
#include <limits>
#include <queue>
#include <cassert>

class UndirectedWeightedGraph
{
public:

    std::vector<std::vector<std::tuple<int, int>>> AdjacencyList;

    int Size;

    UndirectedWeightedGraph(int NodeCount)
    {
        Size = NodeCount;

        for (int Index = 0; Index < Size; ++Index)
        {
            std::vector<std::tuple<int, int>> Neighbors;
            AdjacencyList.push_back(Neighbors);
        }
    }

    void AddEdge(int Src, int Dst, int Weight)
    {
        AdjacencyList[Src].push_back(std::make_tuple(Dst, Weight));
        AdjacencyList[Dst].push_back(std::make_tuple(Src, Weight));
    }
};

std::tuple<std::vector<int>, std::vector<int>> Dijkstras(UndirectedWeightedGraph& Graph, int SrcNode)
{
    std::vector<int> Visited(Graph.Size, false);
    std::vector<int> PrevNodes(Graph.Size, -1);
    std::vector<int> Distances(Graph.Size, std::numeric_limits<int>::max());
    std::priority_queue<
        std::tuple<int, int>,
        std::vector<std::tuple<int, int>>,
        std::greater<std::tuple<int, int>>
    > PQ;

    Distances[SrcNode] = 0;
    PQ.push(std::make_tuple(SrcNode, Distances[SrcNode]));
    
    while (!PQ.empty())
    {
        std::tuple<int, int> Top = PQ.top();
        int Src = std::get<0>(Top);
        int SrcDistance = std::get<1>(Top);
        Visited[Src] = true;
        PQ.pop();

        for (std::tuple<int, int> Edge : Graph.AdjacencyList[Src])
        {
            int Dst = std::get<0>(Edge);
            int ToDstWeight = std::get<1>(Edge);
            int NewDistance = Distances[Src] + ToDstWeight;

            if (Visited[Dst])
            {
                continue;
            }

            if (NewDistance < Distances[Dst])
            {
                PrevNodes[Dst] = Src;
                Distances[Dst] = NewDistance;
                PQ.push(std::make_tuple(Dst, Distances[Dst]));
            }
        }
    }

    return std::make_tuple(Distances, PrevNodes);
}

int main()
{

    UndirectedWeightedGraph Graph { 7 };

    Graph.AddEdge(0,1,2);
    Graph.AddEdge(0,2,6);
    Graph.AddEdge(1,3,5);
    Graph.AddEdge(2,3,8);
    Graph.AddEdge(3,4,10);
    Graph.AddEdge(3,5,15);
    Graph.AddEdge(4,6,2);
    Graph.AddEdge(5,6,6);
    
    std::tuple<std::vector<int>, std::vector<int>> TestOutput = Dijkstras(Graph, 1);
    
    std::vector TestOutputDistance {2, 0, 8, 5, 15, 20, 17};
    assert(std::get<0>(TestOutput) == TestOutputDistance);
    std::vector TestOutputPrevNodes {1, -1, 0, 1, 3, 3, 4};
    assert(std::get<1>(TestOutput) == TestOutputPrevNodes);
    
    std::cout << "PASS";

    return 0;
}
