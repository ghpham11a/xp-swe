class Solution:

    def largest_altitude(self, gain):
        
        alt = 0
        max_alt = 0

        for change in gain:
            alt += change
            max_alt = max(max_alt, alt)

        return max_alt