class Solution(object):

    def find_median_sorted_arrays(self, sm_arr, lg_arr):
        # Ensure that 'sm_arr' is the smaller array.
        # If not, swap the arrays by recursively calling the function
        # with the smaller array as the first argument.
        if len(lg_arr) < len(sm_arr):
            return self.solution(lg_arr, sm_arr)  # Alternatively, this could be a call to a helper like find_median_sorted_arrays(lg_arr, sm_arr)

        # Check that both input arrays are sorted.
        # If either array is not sorted, raise an error.
        if sm_arr != sorted(sm_arr) or lg_arr != sorted(lg_arr):
            raise ValueError("Input arrays must be sorted.")

        # Determine the lengths of the two arrays.
        sm_arr_len = len(sm_arr)
        lg_arr_len = len(lg_arr)

        # 'half_len' represents half of the total number of elements (using floor division).
        # This will be used to determine how many elements should be in the left partition.
        half_len = (sm_arr_len + lg_arr_len) // 2

        # Set up binary search boundaries for the smaller array.
        sm_lo_idx = 0
        sm_hi_idx = sm_arr_len - 1

        # Perform binary search on the smaller array to find the correct partition.
        while True:
            # Choose a partition index for the smaller array (midpoint of the current search range).
            sm_partition_idx = (sm_lo_idx + sm_hi_idx) // 2

            # Determine the corresponding partition index for the larger array.
            # The idea is that the total number of elements in the left partition
            # (from both arrays) should be half_len (or half_len + 1 for odd total counts).
            # (sm_partition_idx + 1) is the number of elements taken from sm_arr in the left partition.
            # Subtracting one more gives the index of the last element in lg_arr's left partition.
            lg_partition_idx = half_len - (sm_partition_idx + 1) - 1

            # Set the left value from sm_arr. If the partition index is invalid (-1), use -infinity.
            sm_lo_value = float("-infinity")
            if sm_partition_idx >= 0:
                sm_lo_value = sm_arr[sm_partition_idx]

            # Set the right value from sm_arr. If there are no elements to the right, use +infinity.
            sm_hi_value = float("infinity")
            if (sm_partition_idx + 1) < len(sm_arr):
                sm_hi_value = sm_arr[sm_partition_idx + 1]

            # Set the left value from lg_arr. If the partition index is invalid (-1), use -infinity.
            lg_lo_value = float("-infinity")
            if lg_partition_idx >= 0:
                lg_lo_value = lg_arr[lg_partition_idx]

            # Set the right value from lg_arr. If there are no elements to the right, use +infinity.
            lg_hi_value = float("infinity")
            if (lg_partition_idx + 1) < len(lg_arr):
                lg_hi_value = lg_arr[lg_partition_idx + 1]

            # Check if we have found the correct partition:
            # - sm_lo_value should be less than or equal to lg_hi_value, and
            # - lg_lo_value should be less than or equal to sm_hi_value.
            if sm_lo_value <= lg_hi_value and lg_lo_value <= sm_hi_value:
                # Correct partition found; now compute the median based on the total number of elements.
                if (sm_arr_len + lg_arr_len) % 2 == 0:
                    # For an even total number of elements, the median is the average of the two middle numbers.
                    return (max(sm_lo_value, lg_lo_value) + min(sm_hi_value, lg_hi_value)) / 2.0
                # For an odd total number of elements, the median is the next element (min(sm_hi_value, lg_hi_value)).
                return min(sm_hi_value, lg_hi_value)
            # If the largest element in the left partition of sm_arr is greater than the smallest element in the right partition of lg_arr,
            # it means we have partitioned too far right in sm_arr. Move the search to the left.
            elif sm_lo_value > lg_hi_value:
                sm_hi_idx = sm_partition_idx - 1
            # Otherwise, the partition is too far left in sm_arr. Move the search to the right.
            else:
                sm_lo_idx = sm_partition_idx + 1

solution = Solution()

assert(solution.find_median_sorted_arrays([1,2], [3,4]) == 2.5)
assert(solution.find_median_sorted_arrays([1,3], [2]) == 2.0)

print("PASS")
