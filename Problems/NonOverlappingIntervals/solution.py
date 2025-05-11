class Solution:

    def erase_overlap_intervals(self, intervals):

        # Sort intervals by their start time (default sort on first element of each pair)
        intervals.sort()

        # Counter to keep track of how many intervals need to be removed
        output = 0

        # Initialize the previous interval's end time with the end of the first interval
        prev_end = intervals[0][1]

        # Iterate through the rest of the intervals
        for start, end in intervals[1:]:
            # If the current interval does not overlap with the previous one
            if start >= prev_end:
                # Move the previous end to the current interval's end
                prev_end = end
            else:
                # Overlap found, need to remove one interval
                output += 1
                # Keep the interval with the earlier end time to reduce future overlaps
                prev_end = min(prev_end, end)

        # Return the total number of intervals removed
        return output

solution = Solution()

assert(solution.erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) == 1)

print("PASS")