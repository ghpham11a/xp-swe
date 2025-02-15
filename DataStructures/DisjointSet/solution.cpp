#include <iostream>
#include <vector>
#include <cassert>

class DisjointSet 
{
public:
    
    std::vector<int> Parent;
    std::vector<int> Rank;

    DisjointSet(int size) 
    {
        for (int i = 0; i < size; ++i) 
        {
            Parent.push_back(i);
            Rank.push_back(1);
        }
    }
    
    int Find(int node) 
    {
        if (Parent[node] == node) {
            Parent[node] = Parent[Parent[node]];
            return Parent[node];
        }
        return Find(Parent[node]);
    }
    
    bool Union(int nodeA, int nodeB) 
    {
        int RootA = Find(nodeA);
        int RootB = Find(nodeB);
        
        if (RootA == RootB) 
        {
            return false;
        }
        
        if (Rank[RootA] > Rank[RootB]) 
        {
            Parent[RootB] = RootA;
            Rank[RootA] += Rank[RootB];
        } 
        else 
        {
            Parent[RootA] = RootB;
            Rank[RootB] += Rank[RootA];
        }
        
        return true;
    }
};

int main() 
{
    
    int edges[7][2] = {{0,2},{1,4},{1,5},{2,3},{2,7},{4,8},{5,8}};
    
    DisjointSet DS(9);
    
    for (auto edge : edges) 
    {
        DS.Union(edge[0], edge[1]);
    }

    std::vector TestOutput { 2, 4, 2, 2, 4, 4, 6, 2, 4 };
    assert(DS.Parent == TestOutput);

    std::cout << "PASS";

    return 0;
}