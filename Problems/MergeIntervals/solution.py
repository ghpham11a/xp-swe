class Solution:

    def merge(self, intervals):
        
        # First, sort the intervals based on their start value.
        # This ensures that when we iterate, each interval's start is not less than the previous one.
        intervals.sort(key = lambda i : i[0])

        # Initialize the output list with the first interval.
        # This is our starting merged interval.
        output = [intervals[0]]

        # Loop through the remaining intervals.
        for start, end in intervals[1:]:

            # Get the end of the last interval in the output list.
            last_end = output[-1][1]

            # If the current interval overlaps with the last merged interval...
            if start <= last_end:
                # ...merge them by updating the end of the last interval.
                # We take the maximum of the last interval's end and the current interval's end.
                output[-1][1] = max(last_end, end)
            else:
                # If there is no overlap, add the current interval as a new interval in the output.
                output.append([start, end])

        return output

solution = Solution()

assert(solution.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]])

print("PASS")