# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 0
        hi = n

        while lo <= hi:

            mid = lo + (hi - lo) // 2

            res = guess(mid)

            if res == 0:
                return mid

            if res == 1:
                lo = mid + 1

            if res == -1:
                hi = mid - 1

        return -1