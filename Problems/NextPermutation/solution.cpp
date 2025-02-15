class Solution 
{
public:
    void NextPermutation(std::vector<int>& Nums) 
    {
        int FirstDecIndex = Nums.size() - 2;

        while (FirstDecIndex >= 0 && Nums[FirstDecIndex + 1] <= Nums[FirstDecIndex])
        {
            FirstDecIndex -= 1;
        }

        if (FirstDecIndex >= 0)
        {
            int NextLargerIndex = Nums.size() - 1;
            while (NextLargerIndex >= 0 && Nums[NextLargerIndex] <= Nums[FirstDecIndex])
            {
                NextLargerIndex -= 1;
            }
            Swap(Nums, FirstDecIndex, NextLargerIndex);
        }

        Reverse(Nums, FirstDecIndex + 1);
    }

    void Reverse(std::vector<int>& Nums, int StartIndex)
    {
        int LeftIndex = StartIndex;
        int RightIndex = Nums.size() - 1;

        while (LeftIndex < RightIndex)
        {
            Swap(Nums, LeftIndex, RightIndex);
            LeftIndex += 1;
            RightIndex -= 1;
        }
    }

    void Swap(std::vector<int>& Nums, int I, int J)
    {
        int temp = Nums[I];
        Nums[I] = Nums[J];
        Nums[J] = temp;
    }
};