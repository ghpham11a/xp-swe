#include <iostream>
#include <vector>
#include <cassert>

int BinarySearch(int Target, std::vector<int> Nums)
{
    
    int Lo = 0;
    int Hi = Nums.size() - 1;
    
    while (Lo <= Hi)
    {
        
        int Mid = Lo + (Hi - Lo) / 2;
        
        if (Nums[Mid] == Target)
        {
            return Mid;
        }
    
        if (Nums[Mid] < Target)
        {
            Lo = Mid + 1;
        }
        
        if (Nums[Mid] > Target)
        {
            Hi = Mid - 1;
        }
    }
    
    return -1;
}

int main() 
{

    std::vector<int> TestInput {2, 3, 4, 10, 40};
    assert(BinarySearch(3, TestInput) == 1);
    
    std::cout << "PASS";

    return 0;
}