def solution(sm_arr, lg_arr):

    if len(lg_arr) < len(sm_arr):
        return find_median_sorted_arrays(lg_arr, sm_arr)

    if sm_arr != sorted(sm_arr) or lg_arr != sorted(lg_arr):
        raise ValueError("Input arrays must be sorted.")

    sm_arr_len = len(sm_arr)
    lg_arr_len = len(lg_arr)
    half_len = (sm_arr_len + lg_arr_len) // 2

    sm_lo_idx = 0
    sm_hi_idx = sm_arr_len - 1

    while True:
        sm_partition_idx = (sm_lo_idx + sm_hi_idx) // 2
        lg_partition_idx = half_len - (sm_partition_idx + 1) - 1

        sm_lo_value = float("-infinity")
        if sm_partition_idx >= 0:
            sm_lo_value = sm_arr[sm_partition_idx]

        sm_hi_value = float("infinity")
        if (sm_partition_idx + 1) < len(sm_arr):
            sm_hi_value = sm_arr[sm_partition_idx + 1]

        lg_lo_value = float("-infinity")
        if lg_partition_idx >= 0:
            lg_lo_value = lg_arr[lg_partition_idx]

        lg_hi_value = float("infinity")
        if (lg_partition_idx + 1) < len(lg_arr):
            lg_hi_value = lg_arr[lg_partition_idx + 1]

        if sm_lo_value <= lg_hi_value and lg_lo_value <= sm_hi_value:
            if (sm_arr_len + lg_arr_len) % 2 == 0:
                return (max(sm_lo_value, lg_lo_value) + min(sm_hi_value, lg_hi_value)) / 2.0
            return min(sm_hi_value, lg_hi_value)
        elif sm_lo_value > lg_hi_value:
            sm_hi_idx = sm_partition_idx - 1
        else:
            sm_lo_idx = sm_partition_idx + 1