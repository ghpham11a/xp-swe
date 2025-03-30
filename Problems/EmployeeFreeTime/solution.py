class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start},{self.end}]"

class Solution(object):

    def employee_free_time(self, schedule):

        output = []

        # Flatten the list of schedules into a single list of intervals.
        intervals = []
        for emp_schedule in schedule:
            for interval in emp_schedule:
                intervals.append([interval.start, interval.end])

        # Sort all intervals by their start time.
        intervals.sort(key=lambda x: x[0])

        # Initialize 'last_end' with the end of the first interval.
        last_end = intervals[0][1]

        # Iterate over the remaining intervals to find gaps (free time).
        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            # If there is a gap between the current interval's start and the previous interval's end,
            # it means we've found a period where all employees are free.
            if curr_start > last_end:
                # Create a new Interval representing the free time from 'last_end' to 'curr_start'.
                output.append(Interval(last_end, curr_start))

            # Update 'last_end' to be the maximum end time encountered so far.
            # This is important for merging overlapping intervals.
            last_end = max(last_end, curr_end)

        return output

def createIntervals(intervals):
    output = []
    for emp_schedule in intervals:
        output.append(list(map(lambda x: Interval(x[0], x[1]), emp_schedule)))
    return output

solution = Solution()

print(solution.employee_free_time(createIntervals([[[1,2],[5,6]],[[1,3]],[[4,10]]])), [Interval(3, 4)])
print(solution.employee_free_time(createIntervals([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]])), [Interval(5, 6), Interval(7, 9)])

print("PASS")

