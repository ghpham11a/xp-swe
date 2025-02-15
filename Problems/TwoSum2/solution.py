class Solution(object):

    def two_sum(self, numbers, target):
        
        left, right = 0, len(numbers) - 1

        while left < right:

            two_sum = numbers[left] + numbers[right]

            if two_sum > target:
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]

solution = Solution()

assert(solution.two_sum([2,7,11,15], 9) == [1,2])

print("PASS")