class Solution:

    def daily_temperatures(self, temperatures):
        
        output = [0] * len(temperatures)

        stack = []

        for curr_day, curr_temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                output[prev_day] = curr_day - prev_day
            stack.append(curr_day)

        return output

solution = Solution()

assert(solution.daily_temperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0])

print("PASS")