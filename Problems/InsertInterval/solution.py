from typing import List

class Solution:

    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        output = []  # This will store the final list of merged intervals

        for i in range(len(intervals)):
            # Case 1: New interval comes completely before the current interval
            # (no overlap), so we can insert it before and return the result.
            if new_interval[1] < intervals[i][0]:
                output.append(new_interval)
                return output + intervals[i:]  # Add the remaining intervals

            # Case 2: New interval comes completely after the current interval
            # (no overlap), so just add the current interval to output.
            elif new_interval[0] > intervals[i][1]:
                output.append(intervals[i])

            # Case 3: New interval overlaps with the current interval,
            # so merge them by updating the start to the min start,
            # and the end to the max end.
            else:
                new_interval = [
                    min(new_interval[0], intervals[i][0]),  # new merged start
                    max(new_interval[1], intervals[i][1])   # new merged end
                ]

        # After processing all intervals, append the (possibly merged) new_interval.
        output.append(new_interval)

        return output  # Return the final merged list

solution = Solution()

assert(solution.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]])

print("PASS")