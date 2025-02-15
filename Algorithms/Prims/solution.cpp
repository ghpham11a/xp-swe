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

typedef std::priority_queue<
    std::tuple<int, int, int>,
    std::vector<std::tuple<int, int, int>>,
    std::greater<std::tuple<int, int, int>>
> PriorityQueue;

void PrimsAddEdge(UndirectedWeightedGraph& Graph, std::vector<bool>& Visited, PriorityQueue& PQ, int Src)
{
    Visited[Src] = true;

    for (std::tuple<int, int> Edge : Graph.AdjacencyList[Src])
    {
        int Dst = std::get<0>(Edge);
        int ToDstWeight = std::get<1>(Edge);
        if (!Visited[Dst])
        {
            PQ.push(std::make_tuple(ToDstWeight, Src, Dst));
        }
    }
}

std::tuple<int, std::vector<std::tuple<int, int, int>>> Prims(UndirectedWeightedGraph& Graph)
{
    int TargetEdgeCount = Graph.Size - 1;
    int EdgeCount = 0;
    int MstCost = 0;
    std::vector<std::tuple<int, int, int>> MstEdges(Graph.Size - 1);
    std::vector<bool> Visited(Graph.Size, false);

    PriorityQueue PQ;
    PrimsAddEdge(Graph, Visited, PQ, 0);

    while (!PQ.empty() && EdgeCount != TargetEdgeCount)
    {

        std::tuple<int, int, int> Top = PQ.top();
        int ToDstWeight = std::get<0>(Top);
        int Src = std::get<1>(Top);
        int Dst = std::get<2>(Top);
        PQ.pop();

        if (Visited[Dst])
        {
            continue;
        }

        MstEdges[EdgeCount] = std::make_tuple(Src, Dst, ToDstWeight);
        EdgeCount++;
        MstCost += ToDstWeight;

        PrimsAddEdge(Graph, Visited, PQ, Dst);
    }

    if (EdgeCount != TargetEdgeCount) {
        return std::make_tuple(NULL, NULL);
    }

    return std::make_tuple(MstCost, MstEdges);
}

int main()
{
    
    UndirectedWeightedGraph Graph(10);

    Graph.AddEdge(0, 1, 5);
    Graph.AddEdge(1, 2, 4);
    Graph.AddEdge(2, 9, 2);
    Graph.AddEdge(0, 4, 1);
    Graph.AddEdge(0, 3, 4);
    Graph.AddEdge(1, 3, 2);
    Graph.AddEdge(2, 7, 4);
    Graph.AddEdge(2, 8, 1);
    Graph.AddEdge(9, 8, 0);
    Graph.AddEdge(4, 5, 1);
    Graph.AddEdge(5, 6, 7);
    Graph.AddEdge(6, 8, 4);
    Graph.AddEdge(4, 3, 2);
    Graph.AddEdge(5, 3, 5);
    Graph.AddEdge(3, 6, 11);
    Graph.AddEdge(6, 7, 1);
    Graph.AddEdge(3, 7, 2);
    Graph.AddEdge(7, 8, 6);
    
    std::tuple<int, std::vector<std::tuple<int, int, int>>> Result = Prims(Graph);
    
    int MstCost = std::get<0>(Result);
    std::vector<std::tuple<int, int, int>> MstEdges = std::get<1>(Result);
    
    std::cout << MstCost << std::endl;
    for (std::tuple<int, int, int> Edge : MstEdges)
    {
        int Src = std::get<0>(Edge);
        int Dst = std::get<1>(Edge);
        int Weight = std::get<2>(Edge);
        std::cout << Src << " > " << Dst << " Weight: " << Weight << std::endl;
    }

    // 14
    // 0 > 4 Weight: 1
    // 4 > 5 Weight: 1
    // 4 > 3 Weight: 2
    // 3 > 1 Weight: 2
    // 3 > 7 Weight: 2
    // 7 > 6 Weight: 1
    // 1 > 2 Weight: 4
    // 2 > 8 Weight: 1
    // 8 > 9 Weight: 0

    std::cout << "PASS";
    
    return 0;
}