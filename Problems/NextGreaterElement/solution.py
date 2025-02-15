class Solution:

    def next_greater_element(self, nums1, nums2):
        nums_1_index = {n: i for i, n in enumerate(nums1)}
        output = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                index = nums_1_index[val]
                output[index] = curr

            if curr in nums_1_index:
                stack.append(curr)

        return output

solution = Solution()

assert(solution.next_greater_element([4,1,2], [1,3,4,2]) == [-1,3,-1])

print("PASS")