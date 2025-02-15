#include <iostream>
#include <tuple>
#include <queue>
#include <string>
#include <cassert>

int main() {
    
    // Create priority queue
    std::priority_queue<
        std::tuple<int, std::string>,
        std::vector<std::tuple<int, std::string>>
    > PQ;
    
    // Add to priority queue
    PQ.push(std::make_tuple(1, "DATA"));
    PQ.push(std::make_tuple(2, "DATA"));
    PQ.push(std::make_tuple(3, "DATA"));
    PQ.push(std::make_tuple(4, "DATA"));
    PQ.push(std::make_tuple(5, "DATA"));
    
    std::vector<std::tuple<int, std::string>> Output;
    while (!PQ.empty())
    {
        // Remove to priority queue
        std::tuple<int, std::string> Top = PQ.top();
        int Key = std::get<0>(Top);
        std::string Data = std::get<1>(Top);
        PQ.pop();
        
        Output.push_back(Top);
    }
    
    std::vector<std::tuple<int, std::string>> TestOutput {
        std::make_tuple(5, "DATA"),
        std::make_tuple(4, "DATA"),
        std::make_tuple(3, "DATA"),
        std::make_tuple(2, "DATA"),
        std::make_tuple(1, "DATA")
    };
    
    assert(Output == TestOutput);

    std::cout << "PASS";
    
    return 0;
}