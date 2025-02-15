#include <unordered_map>
#include <vector>
#include <stdexcept>

enum class Marker: int
{
    Unmarked,
    Temporary,
    Permanent
}; 

class Solution 
{
public:

    string alienOrder(std::vector<string>& Words) 
    {
        std::unordered_map<char, std::vector<char>> Graph;

        if (BuildGraph(Graph, Words) == false)
        {
            return "";
        }
        
        std::unordered_map<char, Marker> Visited;
        std::vector<char> Output;

        try 
        {         
            for (auto itr = Graph.begin(); itr != Graph.end(); ++itr)
            {
                if (Visited[itr->first] == Marker::Unmarked)
                {
                    DFS(Graph, Visited, Output, itr->first);
                }
            }
        } 
        catch(const exception& e)  
        {   
            return "";
        } 

        std::reverse(Output.begin(), Output.end());
        string StringOutput(Output.begin(), Output.end()); 

        return StringOutput;
    }

    void DFS(std::unordered_map<char, std::vector<char>>& Graph, std::unordered_map<char, Marker>& Visited, std::vector<char>& Output, char Node)
    {
        if (Visited[Node] == Marker::Permanent)
        {
            return;
        }

        if (Visited[Node] == Marker::Temporary)
        {
            throw invalid_argument("received negative value"); 
        }

        Visited[Node] = Marker::Temporary;

        for (auto NextNode : Graph[Node])
        {
            DFS(Graph, Visited, Output, NextNode);
        }

        Visited[Node] = Marker::Permanent;
        Output.push_back(Node);
    }

    bool BuildGraph(std::unordered_map<char, std::vector<char>>& Graph, std::vector<string>& Words)
    {
        for (auto Word : Words)
        {
            for (char c : Word)
            {
                std::vector<char> Neighbors;
                Graph.insert({ c, Neighbors });
            }
        }

        for (int i = 0; i < Words.size() - 1; ++i) 
        {
            string Word = Words[i];
            string NextWord = Words[i + 1];
            int MinWordSize = std::min(Word.size(), NextWord.size());
            bool DidBreak = false;
            for (int j = 0; j < MinWordSize; ++j)
            {
                char WordChar;
                char NextWordChar;
                if (j < Word.size()) 
                {
                    WordChar = Word[j];
                }
                if (j < NextWord.size()) 
                {
                    NextWordChar = NextWord[j];
                }

                if (!DidBreak && WordChar != NextWordChar) 
                {
                    Graph[WordChar].push_back(NextWordChar);
                    DidBreak = true;
                    break;
                }
            }

            if (!DidBreak && NextWord.size() < Word.size()) 
            {
                return false;
            }
        }
        return true;
    }
};