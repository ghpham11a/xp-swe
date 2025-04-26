class Solution:
    def maxArea(self, height):
        # Initialize two pointers:
        # 'left' starts at the beginning of the array
        # 'right' starts at the end of the array
        left, right = 0, len(height) - 1

        # Initialize the maximum area to negative infinity (will update as we find larger areas)
        max_area = float("-inf")

        # Continue until the two pointers meet
        while left < right:
            # The height of the container is determined by the shorter of the two lines
            min_height = min(height[left], height[right])
            # The width of the container is the distance between the two lines
            width = (right - left)
            # Calculate the current area and update max_area if it's larger than the previous max
            max_area = max(max_area, min_height * width)

            # Move the pointer pointing to the shorter line inward
            # (because moving the taller one inward cannot increase the height, and we want a chance to find a taller line)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # After checking all possibilities, return the maximum area found
        return max_area