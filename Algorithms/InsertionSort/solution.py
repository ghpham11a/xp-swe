def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        
        value_to_insert = arr[i]
        
        scan_index = i - 1
        
        while scan_index >= 0 and arr[scan_index] > value_to_insert:
            arr[scan_index + 1] = arr[scan_index]
            scan_index -= 1
            
        arr[scan_index + 1] = value_to_insert
        
    return arr

assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert insertion_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]

print("PASS")

