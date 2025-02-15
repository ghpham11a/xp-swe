#include <iostream>
#include <vector>
#include <queue>
#include <cassert>

class DirectedAcyclicGraph
{
public:

    std::vector<std::vector<int>> AdjacencyList;
    int Size;

    DirectedAcyclicGraph(int VertexCount)
    {
        Size = VertexCount;
        for (int Vertex = 0; Vertex < VertexCount; ++Vertex)
        {
            std::vector<int> Neighbors;
            AdjacencyList.push_back(Neighbors);
        }
    }
    
    void AddEdge(int Src, int Dst)
    {
        AdjacencyList[Src].push_back(Dst);
    }
};

std::vector<int> Kahns(UndirectedWeightedGraph& Graph)
{
    std::vector<int> InDegrees(Graph.Size, 0);
    std::queue<int> Queue;
    std::vector<int> Output;

    for (int Node = 0; Node < Graph.Size; ++Node)
    {
        for (int Neighbor : Graph.AdjacencyList[Node])
        {
            InDegrees[Neighbor] += 1;
        }
    }

    for (int Node = 0; Node < Graph.Size; ++Node)
    {
        if (InDegrees[Node] == 0)
        {
            Queue.push(Node);
        }
    }

    while (!Queue.empty())
    {
        int Node = Queue.front();
        Queue.pop();

        Output.push_back(Node);

        for (int Neighbor : Graph.AdjacencyList[Node])
        {
            InDegrees[Neighbor] -= 1
            if (InDegrees[Neighbor] == 0)
            {
                Queue.push(Neighbor);
            }
        }
    }

    return Output;
}

int main()
{

    UndirectedWeightedGraph Graph;

    Graph.AddEdge(0, 2);
    Graph.AddEdge(0, 3);
    Graph.AddEdge(0, 6);
    Graph.AddEdge(1, 4);
    Graph.AddEdge(2, 6);
    Graph.AddEdge(3, 1);
    Graph.AddEdge(3, 4);
    Graph.AddEdge(4, 5);
    Graph.AddEdge(4, 8);
    Graph.AddEdge(6, 7);
    Graph.AddEdge(6, 11);
    Graph.AddEdge(7, 4);
    Graph.AddEdge(7, 12);
    Graph.AddEdge(9, 2);
    Graph.AddEdge(9, 10);
    Graph.AddEdge(10, 6);
    Graph.AddEdge(11, 12);
    Graph.AddEdge(12, 8);

    std::vector<int> TestOutput{0, 9, 13, 3, 2, 10, 1, 6, 7, 11, 4, 12, 5, 8};
    assert(Kahns(Graph) == TestOutput);

    std::cout << "PASS";

    return 0;
}

