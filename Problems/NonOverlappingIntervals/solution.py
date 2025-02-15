class Solution:

    def erase_overlap_intervals(self, intervals):

        intervals.sort()

        output = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                output += 1
                prev_end = min(prev_end, end)


        return output

solution = Solution()

assert(solution.erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) == 1)

print("PASS")