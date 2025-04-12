def merge_sort(nums):

    if len(nums) < 2:
        return nums
    
    output = []

    middle = len(nums) // 2

    left_list = merge_sort(nums[:middle])
    right_list = merge_sort(nums[middle:])

    left_index = 0
    right_index = 0

    while (left_index < len(left_list)) and (right_index < len(right_list)):
        if left_list[left_index] < right_list[right_index]:
            output.append(left_list[left_index])
            left_index += 1
        else:
            output.append(right_list[right_index])
            right_index += 1

    output += left_list[left_index:]
    output += right_list[right_index:]

    return output


def merge_sort(nums):
    # Base case: if the list is empty or contains only one element, it's already sorted.
    if len(nums) < 2:
        return nums
    
    # Initialize an empty list to store the merged sorted result.
    result = []
    
    # Compute the middle index of the list using integer division.
    middle = len(nums) // 2
    
    # Recursively sort the left half of the list.
    left_list = merge_sort(nums[0:middle])
    # Recursively sort the right half of the list.
    right_list = merge_sort(nums[middle:])
    
    # Initialize indices to track the current element in each sorted half.
    left_index = 0
    right_index = 0
    
    # Merge the two sorted halves into the result list.
    # Continue merging until one of the halves is exhausted.
    while (left_index < len(left_list) and right_index < len(right_list)):
        # Compare the current elements of both halves.
        if left_list[left_index] < right_list[right_index]:
            # Append the smaller element from the left half.
            result.append(left_list[left_index])
            # Move to the next element in the left half.
            left_index += 1
        else:
            # Append the smaller element from the right half.
            result.append(right_list[right_index])
            # Move to the next element in the right half.
            right_index += 1
            
    # If there are remaining elements in the left half, append them.
    result += left_list[left_index:]
    # Similarly, if there are remaining elements in the right half, append them.
    result += right_list[right_index:]
    
    # Return the fully merged and sorted list.
    return result

assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert merge_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]

print("PASS")