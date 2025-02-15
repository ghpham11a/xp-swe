#include <iostream>
#include <vector>
#include <cassert>
#include <stack>
#include <algorithm>

class DirectedGraph
{
public:

    std::vector<std::vector<int>> AdjacencyList;
    int Size;

    DirectedGraph(int VertexCount)
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

#define Unvisted -1

void TarjansDFS(DirectedGraph& Graph, int& Time, std::vector<int>& InTimes, std::vector<int>& LowLinks, std::vector<bool>& InStack, std::stack<int>& Stack, int Node)
{
    Stack.push(Node);
    InStack[Node] = true;
    Time++;
    LowLinks[Node] = Time;
    InTimes[Node] = Time;

    for (int Neighbor : Graph.AdjacencyList[Node])
    {
        if (InTimes[Neighbor] == Unvisted)
        {
            TarjansDFS(Graph, Time, InTimes, LowLinks, InStack, Stack, Neighbor);
        }

        if (InStack[Neighbor])
        {
            LowLinks[Node] = std::min(LowLinks[Node], LowLinks[Neighbor]);
        }
    }

    if (InTimes[Node] == LowLinks[Node])
    {
        while (!Stack.empty()) 
        {
            int StackNode = Stack.top();
            Stack.pop();

            InStack[StackNode] = false;
            LowLinks[StackNode] = InTimes[Node];
            if (StackNode == Node)
            {
                break;
            }
        }
    }
}

std::vector<int> Tarjans(DirectedGraph& Graph)
{
    int Time = 0;
    std::vector<int> InTimes(Graph.Size, Unvisted);
    std::vector<int> LowLinks(Graph.Size, 0);
    std::vector<bool> InStack(Graph.Size, false);
    std::stack<int> Stack;

    for (int Node = 0; Node < Graph.Size; ++Node)
    {
        if (InTimes[Node] == Unvisted)
        {
            TarjansDFS(Graph, Time, InTimes, LowLinks, InStack, Stack, Node);
        }
    }

    return LowLinks;
}

int main()
{

    DirectedGraph Graph(8);

    Graph.AddEdge(6, 0);
    Graph.AddEdge(6, 2);
    Graph.AddEdge(3, 4);
    Graph.AddEdge(6, 4);
    Graph.AddEdge(2, 0);
    Graph.AddEdge(0, 1);
    Graph.AddEdge(4, 5);
    Graph.AddEdge(5, 6);
    Graph.AddEdge(3, 7);
    Graph.AddEdge(7, 5);
    Graph.AddEdge(1, 2);
    Graph.AddEdge(7, 3);
    Graph.AddEdge(5, 0);

    std::vector<int> TestOutput{1, 1, 1, 4, 5, 5, 5, 4};

    assert(Tarjans(Graph) == TestOutput);

    std::cout << "PASS";

    return 0;
}
