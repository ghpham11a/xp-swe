from typing import List

def find_pivot(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:

        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return left

