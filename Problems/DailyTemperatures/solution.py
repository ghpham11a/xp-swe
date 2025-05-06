from typing import List

class Solution:

    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        
        # Initialize the output array with all 0s (default wait time is 0)
        # Each position will eventually hold the number of days to wait for a warmer temperature
        output = [0] * len(temperatures)

        # Stack to keep track of temperatures that haven't yet found a warmer day
        # Each element in the stack is a pair: [temperature, index]
        stack = []

        # Iterate over each temperature along with its index
        for i, t in enumerate(temperatures):
            
            # While the current temperature is higher than the temperature at the top of the stack
            # That means we found a warmer day for the temperature at stack[-1]
            while stack and t > stack[-1][0]:
                stack_temp, stack_index = stack.pop()  # Pop the cooler temperature
                output[stack_index] = i - stack_index  # Calculate the number of days waited
            
            # Push the current temperature and its index onto the stack
            # We'll resolve it later when a warmer day is found
            stack.append([t, i])

        # Return the final output array
        return output

solution = Solution()

assert(solution.daily_temperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0])

print("PASS")