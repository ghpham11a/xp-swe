#include <vector>
#include <cassert>

class DisjointSet
{
public:
    std::vector<int> Parent;
    std::vector<int> Rank;
    int Size;

    DisjointSet(int S)
    {
        Size = S;

        for (int i = 0; i < S; ++i)
        {
            Parent.push_back(i);
            Rank.push_back(1);
        }
    }

    int Find(int Node)
    {
        if (Parent[Node] == Node)
        {
            Parent[Node] = Parent[Parent[Node]];
            return Parent[Node];
        }
        return Find(Parent[Node]);
    }

    bool Union(int NodeA, int NodeB)
    {
        int RootA = Find(NodeA);
        int RootB = Find(NodeB);

        if (RootA == RootB)
        {
            return false;
        }

        if (Rank[RootA] > Rank[RootB])
        {
            Rank[RootB] = RootA;
            Rank[RootA] += 1;
        }   
        else
        {
            Rank[RootA] = RootB;
            Rank[RootB] += 1;
        }

        return true;
    }
};

class Solution
{
public:

    int CountComponents(int N, std::vector<std::vector<int>> Edges)
    {
        DisjointSet DS(N);

        int Output = N;

        for (std::vector<int> Edge : Edges)
        {
            if (DS.Union(Edge[0], Edge[1]))
            {
                Output -= 1;
            }
        }

        return Output;
    }

};

int main()
{

    Solution Runner;

    std::vector<std::vector<int>> TestInput{{0,1},{1,2},{3,4}};
    assert(Runner.CountComponents(5, TestInput) == 2);

    std::cout << "PASS";

    return 0;
}