#include <iostream>
#include <vector>
#include <algorithm>

class DirectedGraph
{
public:

    std::vector<std::vector<int>> AdjacencyList;
    int Size;

    DirectedGraph(int VertexCount)
    {
        Size = VertexCount;
        for (int Vertex = 0; Vertex < Size; ++Vertex)
        {
            std::vector<int> Neighbor;
            AdjacencyList.push_back(Neighbor);
        }
    }

    void AddEdge(int Src, int Dst)
    {
        AdjacencyList[Src].push_back(Dst);
    }
};

void FindEulerianPathDFS(DirectedGraph& Graph, std::vector<int>& Output, int Node)
{

    while (!Graph.AdjacencyList[Node].empty())
    {
        int Dst = Graph.AdjacencyList[Node].back();
        Graph.AdjacencyList[Node].pop_back();

        FindEulerianPathDFS(Graph, Output, Dst);
    }

    Output.push_back(Node);
}

std::vector<int> FindEulerianPath(DirectedGraph& Graph)
{
    std::vector<int> Output;

    FindEulerianPathDFS(Graph, Output, 1);
    
    std::reverse(Output.begin(), Output.end());

    return Output;
}

int main()
{

    DirectedGraph Graph(7);

    Graph.AddEdge(1,2);
    Graph.AddEdge(1,3);
    Graph.AddEdge(2,2);
    Graph.AddEdge(2,4);
    Graph.AddEdge(2,4);
    Graph.AddEdge(3,1);
    Graph.AddEdge(3,2);
    Graph.AddEdge(3,5);
    Graph.AddEdge(4,3);
    Graph.AddEdge(4,6);
    Graph.AddEdge(5,6);
    Graph.AddEdge(6,3);

    std::vector<int> Result = FindEulerianPath(Graph);

    for (auto Node : Result)
    {
        std::cout << Node << " ";
    }

    return 0;
}

