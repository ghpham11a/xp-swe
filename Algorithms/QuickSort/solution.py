def quick_sort(arr, left=None, right=None):
    # Initialize left and right bounds if they are not provided
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    # Only proceed if there is more than one element in the current partition
    if left < right:
        # Partition the array around a pivot and get the index of the pivot
        partition_index = partition(arr, left, right)

        # Recursively sort the left partition (elements before the pivot)
        quick_sort(arr, left, partition_index - 1)
        # Recursively sort the right partition (elements after the pivot)
        quick_sort(arr, partition_index + 1, right)

    # After all recursion, if we are at the top-level call, return the array.
    # The condition (right - left) == (len(arr) - 1) checks whether the current bounds
    # span the entire array.
    if (right - left) == (len(arr) - 1):
        return arr


def partition(arr, left, right):
    # Select the pivot as the rightmost element of the current partition
    pivot = arr[right]
    # Initialize the pivot_index which will track the correct placement for the pivot
    pivot_index = left
    
    # Iterate through the array from left to right-1
    for scan_index in range(left, right):
        # If the current element is less than or equal to the pivot,
        # swap it to the front of the partition (at pivot_index),
        # and increment the pivot_index.
        if arr[scan_index] <= pivot:
            swap(arr, pivot_index, scan_index)
            pivot_index += 1
            
    # Swap the pivot element with the element at the pivot_index
    # so that the pivot is placed in its correct sorted position.
    swap(arr, pivot_index, right)
    
    # Return the pivot_index, which is now the correct index of the pivot
    return pivot_index


def swap(arr, index_one, index_two):
    # Swap the elements at the specified indices in the array
    arr[index_one], arr[index_two] = arr[index_two], arr[index_one]