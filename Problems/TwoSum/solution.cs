using System;
using System.Collections.Generic;

public class TwoSum
{
    public static void Main(string[] args)
    {
        int[] testOne = solution(new int[]{2, 7, 11, 15}, 9);
        int[] testTwo = solution(new int[]{3, 2, 4}, 6);
        int[] testThree = solution(new int[]{3, 3}, 6);
    }

    public static int[] solution(int[] nums, int target)
    {
        Dictionary<int, int> map = new Dictionary<int, int>();

        for (int i = 0; i < nums.length; i++)
        {
            int diff = target - nums[i];
            if (map.ContainsKey(diff))
            {
                return new int[]{i, map[diff]};
            }
            map.Add(nums[i], i);
        }

        return new int[] {};
    }
}