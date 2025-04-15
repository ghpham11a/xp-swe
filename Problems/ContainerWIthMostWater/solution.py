class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        max_area = float("-inf")

        while left < right:
            min_height = min(height[left], height[right])
            width = (right - left)
            max_area = max(max_area, min_height * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area