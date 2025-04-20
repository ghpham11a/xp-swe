class Solution:

    def findDifference(self, nums1, nums2):

        nums1_manifest = set(nums1)
        nums2_manifest = set(nums2)
        seen = set()

        num1_not_in_num2 = []
        for num in nums1:
            if num not in nums2_manifest and num not in seen:
                seen.add(num)
                num1_not_in_num2.append(num)

        seen = set()

        num2_not_in_num1 = []
        for num in nums2:
            if num not in nums1_manifest and num not in seen:
                seen.add(num)
                num2_not_in_num1.append(num)

        return [num1_not_in_num2, num2_not_in_num1]