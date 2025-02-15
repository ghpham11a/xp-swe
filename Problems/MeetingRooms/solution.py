class Solution:
    
    def can_attend_meetings(self, intervals):

        intervals.sort()

        for i in range(1, len(intervals)):

            curr_start = intervals[i][0]
            prev_end = intervals[i - 1][1]

            if curr_start < prev_end:
                return False
        
        return True

solution = Solution()

assert(solution.can_attend_meetings([[0,30],[5,10],[15,20]]) == False)

print("PASS")