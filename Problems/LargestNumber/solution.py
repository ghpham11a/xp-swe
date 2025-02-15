import functools

class Solution(object):

    def largest_number(self, nums):

        for index, num in enumerate(nums):
            nums[index] = str(num)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=functools.cmp_to_key(compare))

        return str(int("".join(nums)))


runner = Solution()

print(runner.largest_number([10, 2]))

