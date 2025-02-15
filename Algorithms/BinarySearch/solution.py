def binary_search(target, nums):
    
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:

        mid = lo + (hi - lo) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            lo = mid + 1
 
        if nums[mid] > target:
            hi = mid - 1

    return -1


assert(binary_search(3, [2, 3, 4, 10, 40]) == 1)

print("PASS")