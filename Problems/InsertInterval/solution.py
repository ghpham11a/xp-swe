class Solution:

    def insert(self, intervals, new_interval):
        output = []

        for i in range(len(intervals)):
            if new_interval[1] < intervals[i][0]:
                output.append(new_interval)
                return output + intervals[i:]
            elif new_interval[0] > intervals[i][1]:
                output.append(intervals[i])
            else:
                new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]

        output.append(new_interval)

        return output

solution = Solution()

assert(solution.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]])

print("PASS")