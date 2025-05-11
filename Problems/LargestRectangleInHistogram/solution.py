from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # Stack will store tuples of (start_index, height)

        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):
            start = i  # Initialize start index for the current bar

            # If the current bar is lower than the bar on top of the stack,
            # pop from the stack and calculate area with popped height
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))  # Calculate area
                start = index  # Extend the start to the left as far as popped bar started

            # Push the current bar along with its (possibly updated) start index
            stack.append((start, h))

        # Final pass: calculate area for all remaining bars in the stack
        # These bars extend to the end of the histogram
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))  # Width is from start to end

        return max_area  # Return the maximum area found