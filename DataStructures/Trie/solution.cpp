#include <iostream>
#include <unordered_map>
#include <string>
#include <cassert>
#include <vector>

struct TrieNode
{
    std::unordered_map<char, TrieNode> Children;
    bool IsEnd;
    
    TrieNode()
    {
        IsEnd = false;
    }
};

class Trie
{
public:
    TrieNode Root;
    
    void Insert(std::string Word)
    {
        TrieNode* CurrNode = &Root;
        for (char& Letter : Word)
        {
            if (CurrNode->Children.find(Letter) == CurrNode->Children.end())
            {
                CurrNode->Children[Letter] = TrieNode();
            }
            CurrNode = &CurrNode->Children[Letter];
        }
        CurrNode->IsEnd = true;
    }
    
    bool Delete(std::string Word)
    {
        
        std::vector<TrieNode*> Parents;
        
        TrieNode* CurrNode = &Root;
        Parents.push_back(CurrNode);
        
        for (char& Letter : Word)
        {
            if (CurrNode->Children.find(Letter) == CurrNode->Children.end())
            {
                return false;
            }
            CurrNode = &CurrNode->Children[Letter];
            Parents.push_back(CurrNode);
        }
        
        CurrNode->IsEnd = false;
        
        Parents.pop_back();
        
        for (int ParentAndWordIndex = Parents.size() - 1; ParentAndWordIndex >= 0; --ParentAndWordIndex)
        {
            
            TrieNode* Parent = Parents[ParentAndWordIndex];
            char CurrChar = Word[ParentAndWordIndex];
            
            if (Parent->Children[CurrChar].IsEnd == false && Parent->Children[CurrChar].Children.size() == 0)
            {
                Parent->Children.erase(CurrChar);
            }
        }
    }
    
    bool Search(std::string Word)
    {
        TrieNode* CurrNode = &Root;
        for (char& Letter : Word)
        {
            if (CurrNode->Children.find(Letter) == CurrNode->Children.end())
            {
                return false;
            }
            CurrNode = &CurrNode->Children[Letter];
        }
        return CurrNode->IsEnd;
    }
};

int main() {
    
    Trie trie;
    
    trie.Insert("Hello");
    
    assert(trie.Search("Hello") == true);
    assert(trie.Search("World") == false);
    assert(trie.Delete("Hello") == true)
    
    std::cout << "PASS";    

    return 0;
}