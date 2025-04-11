def insertion_sort(arr):
    
    arr_len = len(arr)
    
    for i in range(1, arr_len):
        
        value_to_insert = arr[i]
        
        scan_index = i - 1
        
        while scan_index >= 0 and value_to_insert < arr[scan_index]:
            arr[scan_index + 1] = arr[scan_index]
            scan_index -= 1
            
        arr[scan_index + 1] = value_to_insert
        
    return arr