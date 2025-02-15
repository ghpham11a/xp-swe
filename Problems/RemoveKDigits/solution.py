class Solution:

    def remove_k_digits(self, num, k):
        stack = []

        for c in num:

            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()

            stack.append(c)

        stack = stack[:len(stack) - k]

        output = "".join(stack).lstrip('0') or "0"

        return output

solution = Solution()

assert(solution.remove_k_digits("1432219", 3) == "1219")

print("PASS")