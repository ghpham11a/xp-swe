class Solution:

    def sum_subarray_mins(self, arr):
        MOD = 10 ** 9 + 7
        output = 0
        stack = []

        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                output = (output + m * left * right) % MOD
            stack.append((i, n))

        for i in range(len(stack)):
            j , n = stack[i]
            left = j - stack[i - 1][0] if i > 0 else j + 1
            right = len(arr) - j
            output = (output + n * left * right) % MOD

        return output

solution = Solution()

assert(solution.sum_subarray_mins([3,1,2,4]) == 17)

print("PASS")