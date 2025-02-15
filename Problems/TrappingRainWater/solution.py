class Solution(object):

    def trap(self, heights):
        left = 0
        right = len(heights) - 1
        left_wall = 0
        right_wall = 0
        water = 0
        
        while left < right:
            if heights[left] < heights[right]:
                if heights[left] > left_wall:
                    left_wall = heights[left]
                else:
                    water += left_wall - heights[left]
                left += 1
            else:
                if heights[right] > right_wall:
                    right_wall = heights[right]
                else:
                    water += right_wall - heights[right]
                right -= 1
        
        return water

solution = Solution()

assert(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6)

print("PASS")