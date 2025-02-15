// Online C++ compiler to run C++ program online
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int solution(std::string &s)
{
    std::map<char, int> seenCharacters;
    int left = 0;
    int result = 0;
    
    for (int right = 0; right < s.length(); i++)
    {
        char currentChar = s[i];
        if (seenCharacters.count(currentChar) && seenCharacters[currentChar] >= left)
        {
            left = seenCharacters[currentChar] + 1;
        }
        else
        {
            result = std::max(result, right - left + 1);
        }
        seenCharacters.insert({currentChar, right});
    }
    
    return 1;
}

int main()
{
    std::string hello = "Hello World";
    
    solution(hello);
    
    return 0;
}