from typing import List
import math

class Solution:

    def min_eating_speed(self, piles, h):
        # The maximum possible eating speed is the size of the largest pile.
        # If Koko eats at this speed, she can finish each pile in one hour.
        output_max = max(piles)

        # Initialize the result with the maximum possible value
        output = output_max

        # Set the binary search boundaries:
        # Minimum speed is 1 banana/hour, max is the size of the largest pile
        lo = 1
        hi = output_max

        # Binary search for the smallest valid eating speed
        while lo <= hi:
            # Try the middle speed
            k = lo + (hi - lo) // 2

            # Calculate how many total hours it would take Koko to eat all bananas at speed k
            hours = 0
            for pile in piles:
                # Use math.ceil to compute the number of hours needed for each pile
                hours += math.ceil(pile / k)

            # If Koko can eat all bananas in h or fewer hours at speed k
            if hours <= h:
                # k is a valid speed, try to find a smaller one
                output = min(output, k)
                hi = k - 1
            else:
                # k is too slow, increase speed
                lo = k + 1

        # Return the minimum valid eating speed
        return output

solution = Solution()

assert(solution.min_eating_speed([3,6,7,11], 8) == 4)

print("PASS")