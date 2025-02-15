def kadanes(nums):
    best_sum = float("-inf")
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
        
    return best_sum

assert(kadanes([-2, -3, 4, -1, -2, 1, 5, -3]) == 7)

print("PASS")