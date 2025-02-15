class Solution:
    def findInMountainArray(self, target, mountain_arr):

        arr_len = mountain_arr.length()

        lo_index = 1
        hi_index = arr_len - 2
        mid_index = 0

        while lo_index <= hi_index:
            mid_index = lo_index + (hi_index - lo_index) // 2

            left = mountain_arr.get(mid_index - 1)
            mid = mountain_arr.get(mid_index)
            right = mountain_arr.get(mid_index + 1)

            if left < mid < right:
                lo_index = mid_index + 1
            elif left > mid > right:
                hi_index = mid_index - 1
            else:
                break

        peak = mid_index

        lo_index = 0
        hi_index = peak

        while lo_index <= hi_index:
            mid_index = lo_index + (hi_index - lo_index) // 2
            val = mountain_arr.get(mid_index)

            if val == target:
                return mid_index

            if val < target:
                lo_index = mid_index + 1

            if val > target:
                hi_index = mid_index - 1


        lo_index = peak
        hi_index = arr_len - 1

        while lo_index <= hi_index:
            mid_index = lo_index + (hi_index - lo_index) // 2
            val = mountain_arr.get(mid_index)

            if val == target:
                return mid_index

            if val > target:
                lo_index = mid_index + 1

            if val < target:
                hi_index = mid_index - 1

        return -1

