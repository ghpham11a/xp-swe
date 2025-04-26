class Solution:
    def merge(self, nums1, m, nums2, n):

        p1 = m - 1
        p2 = n - 1

        for last in range(m + n - 1, -1, -1):
            # If nums1 is exhausted, copy remaining nums2 elements
            if p1 < 0:
                nums1[last] = nums2[p2]
                p2 -= 1
            # If nums2 is exhausted, remaining nums1 elements are already in place
            elif p2 < 0:
                break
            elif nums1[p1] >= nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1
            else:
                nums1[last] = nums2[p2]
                p2 -= 1