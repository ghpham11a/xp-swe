class SparseVector:
    def __init__(self, nums):
        self.non_zeroes = {}
        for index, num in enumerate(nums):
            if num != 0:
                self.non_zeroes[index] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        output = 0
        for index, num in self.non_zeroes.items():
            if index in vec.non_zeroes:
                output += (num * vec.non_zeroes[index])
        return output

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)