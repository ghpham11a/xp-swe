#include <iostream>
#include <unordered_map>
#include <string>

int main() {
    
    // Create HashMap
    std::unordered_map<std::string, int> Map;
    
    // Add to HashMap
    Map["ALPHA"] = 10; 
    Map["BRAVO"] = 20; 
    Map["CHARLIE"] = 30; 
    
    // Check if HashMap contains key
    if (Map.find("ALPHA") != Map.end()) 
    {
        
    }
    
    // Get value from HashMap
    int GetValue = Map["ALPHA"];
    
    // Delete key from HashMap
    Map.erase("ALPHA"); 
    
    // Iterate through keys in HashMap

    
    // Iterate through values in HashMap

    
    // Iterate through keys and values in HashMap
    for (auto& KeyValue: Map) {
        std::cout << KeyValue.first << " => " << KeyValue.second << std::endl;
    }

    return 0;
}

