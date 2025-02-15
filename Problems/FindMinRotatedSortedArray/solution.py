def solution(nums):

    res = nums[0]
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        if nums[lo] < nums[hi]:
            return min(res, nums[lo])

        mid = (lo + hi) // 2
        res = min(res, nums[mid])

        if nums[mid] >= nums[lo]:
            lo = mid + 1
        else:
            hi = mid - 1

    return result