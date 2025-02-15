class Solution:

    def minMeeting_rooms(self, intervals):
        
        intervals.sort()

        start_times = [times[0] for times in intervals]
        start_times.sort()

        end_times = [times[1] for times in intervals]
        end_times.sort()

        output = 0
        count = 0

        start_index = 0
        end_index = 0

        while start_index < len(intervals):
            if start_times[start_index] < end_times[end_index]:
                start_index += 1
                count += 1
            else:
                end_index += 1
                count -= 1

            output = max(output, count)

        return output

solution = Solution()

assert(solution.can_attend_meetings([[0,30],[5,10],[15,20]]) == 2)

print("PASS")

