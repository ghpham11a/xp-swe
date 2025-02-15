#include <vector>
#include <tuple>
#include <limits>

class DirectedWeightedGraph
{
public:
    int Size;
    std::vector<std::vector<std::tuple<int, int>>> AdjacencyList;

    DirectedWeightedGraph(int S)
    {
        Size = S;
        for (int Node = 0; Node < Size; ++Node)
        {
            std::vector<std::tuple<int, int>> Neighbors;
            AdjacencyList.push_back(Neighbors);
        }
    }

    void AddEdge(int Src, int Dst, int Weight)
    {
        AdjacencyList[Src].push_back(std::make_tuple(Dst, Weight));
    }

    std::vector<std::tuple<int, int, int>> GetEdges()
    {
        std::vector<std::tuple<int, int, int>> Output;

        for (int Src = 0; Src < AdjacencyList.size(); ++Src)
        {
            for (std::tuple<int, int> Neighbor : AdjacencyList[Src])
            {
                int Dst = std::get<0>(Neighbor);
                int DstWeight = std::get<1>(Neighbor);
                Output.push_back(std::make_tuple(Src, Dst, DstWeight));
            }
        }

        return Output;
    }
};

std::tuple<std::vector<int>, std::vector<int>> BellmanFord(DirectedWeightedGraph& Graph, int Start)
{
    std::vector<int> Distances(Graph.Size, std::numeric_limit<int>::max());
    std::vecotr<int> Predecessor(Graph.Size, NULL);

    std::vector<std::tuple<int, int, int>> Edges = Graph.GetEdges();

    for (int Src = 0; Src < Graph.Size - 1; ++Src)
    {
        for (std::vector<std::tuple<int, int, int>> Edge : Edges)
        {
            int Src = std::get<0>(Edge);
            int Dst = std::get<1>(Edge);
            int ToDstWeight = std::get<2>(Edge);

            if (Distances[Src] + ToDstWeight < Distances[Dst])
            {
                Distances[Dst] = Distances[Src] + ToDstWeight;
                Predecessor[Dst] = Src;
            }
        }
    }

    for (int Src = 0; Src < Graph.Size - 1; ++Src)
    {
        for (std::vector<std::tuple<int, int, int>> Edge : Edges)
        {
            int Src = std::get<0>(Edge);
            int Dst = std::get<1>(Edge);
            int ToDstWeight = std::get<2>(Edge);

            if (Distances[Src] + ToDstWeight < Distances[Dst])
            {
                Distances[Dst] = std::numeric_limit<int>::min();
            }
        }
    }

    return std::make_tuple(Distances, Predecessor);
}

int main()
{

    DirectedWeightedGraph Graph{9};

    Graph.AddEdge(0, 1, 1);
    Graph.AddEdge(1, 2, 1);
    Graph.AddEdge(2, 4, 1);
    Graph.AddEdge(4, 3, -3);
    Graph.AddEdge(3, 2, 1);
    Graph.AddEdge(1, 5, 4);
    Graph.AddEdge(1, 6, 4);
    Graph.AddEdge(5, 6, 5);
    Graph.AddEdge(6, 7, 4);
    Graph.AddEdge(5, 7, 3);


    std::tuple<std::vector<int>, std::vector<int>> Result =  BellmanFord(Graph, 0);

    std::vector<int> TestDistancesOutput = std::get<0>(Result);
    std::vector<int> TestPredecessorOutput = std::get<1>(Result);

    return 0;
}

