#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <stdexcept>

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

enum class Marker: int
{
    Unmarked,
    Temporary,
    Permanent
};

void TopologicalSortDFS(int Node, DirectedAcyclicGraph& Graph, std::vector<int>& Output, std::vector<Marker>& Markers)
{
    if (Markers[Node] == Marker::Permanent)
    {
        return;
    }

    if (Markers[Node] == Marker::Temporary)
    {
        throw std::invalid_argument("Cycle detected"); 
    }

    Markers[Node] = Marker::Temporary;

    for (int Neighbor : Graph.AdjacencyList[Node])
    {
        TopologicalSortDFS(Neighbor, Graph, Output, Markers);
    }
    
    Markers[Node] = Marker::Permanent;
    Output.push_back(Node);
}

std::vector<int> TopologicalSort(DirectedAcyclicGraph& Graph)
{
    std::vector<Marker> Markers(Graph.Size, Marker::Unmarked);
    std::vector<int> Output;
    
    for (int Node = 0; Node < Graph.Size; ++Node)
    {
        if (Markers[Node] == Marker::Unmarked)
        {
            TopologicalSortDFS(Node, Graph, Output, Markers);
        }
    }
    
    std::reverse(Output.begin(), Output.end());
    
    return Output;
}

int main() 
{
    DirectedAcyclicGraph Graph { 7 };
    
    Graph.AddEdge(0,1);
    Graph.AddEdge(0,2);
    Graph.AddEdge(0,5);
    Graph.AddEdge(1,3);
    Graph.AddEdge(1,2);
    Graph.AddEdge(2,3);
    Graph.AddEdge(2,4);
    Graph.AddEdge(3,4);
    Graph.AddEdge(5,4);

    // [6, 0, 5, 1, 2, 3, 4]
    
    std::vector<int> solution = TopologicalSort(Graph);
    
    for (int x : solution)
    {
        std::cout << x << " ";
    }
    
    std::cout << "PASS";

    return 0;
}