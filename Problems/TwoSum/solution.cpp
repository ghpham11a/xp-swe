#include <iostream>
#include <vector>
#include <map>

std::vector<int> solution(std::vector<int> nums, int target)
{
    std::map<int, int> dict;
    
    for (int index = 0; index < nums.size(); ++index)
    {
        int diff = target - nums[index];
        if (dict.count(diff))
        {
            std::vector<int> result{dict[diff], index};
            return result;
        }
        dict.insert({nums[index], index});
    }
    
    std::vector<int> emptyResult{};
    return emptyResult;
}

void printVector(std::vector<int> nums)
{
    for (auto& it : nums)
    {
        std::cout << it << std::endl;
    }
}

int main() {
    
    std::vector<int> testOneNums{ 2, 7, 11, 15 };
    std::vector<int> testOne = twoSum(testOneNums, 9);
    printVector(testOne);

    return 0;
}