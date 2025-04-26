
class Solution:

    def successful_pairs(self, spells, potions, success):

        output = []

        potions.sort()

        for spell in spells:

            lo = 0
            hi = len(potions) - 1
            weakest = len(potions)

            while lo <= hi:

                mid = lo + (hi - lo) // 2

                trial = spell * potions[mid]

                if trial >= success:
                    hi = mid - 1
                    weakest = mid
                else:
                    lo = mid + 1

            output.append(len(potions) - weakest)

        return output