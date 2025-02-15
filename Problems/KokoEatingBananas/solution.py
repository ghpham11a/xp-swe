class Solution:

    def min_eating_speed(self, piles, h):
        
        output_max = max(piles)
        output = output_max

        lo = 1
        hi = output_max

        while lo <= hi:

            k = lo + (hi - lo) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                output = min(output, k)
                hi = k - 1
            else:
                lo = k + 1

        return output

solution = Solution()

assert(solution.min_eating_speed([3,6,7,11], 8) == 4)

print("PASS")