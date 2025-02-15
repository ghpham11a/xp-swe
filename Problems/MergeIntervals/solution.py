class Solution:

    def merge(self, intervals):
        
        intervals.sort(key = lambda i : i[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = output[-1][1]

            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])

        return output

solution = Solution()

assert(solution.max_sub_array([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]])

print("PASS")