from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Special case: if the flowerbed has only one plot
        if len(flowerbed) == 1:
            # Either no flower needs to be planted or the plot is empty
            return n <= 0 or flowerbed[0] == 0

        last_index = len(flowerbed) - 1  # Store last index for later checks

        # Iterate through each plot in the flowerbed
        for flower_index in range(len(flowerbed)):
            is_current_empty = flowerbed[flower_index] == 0  # Check if current plot is empty

            # Check for the first plot (special boundary condition)
            if flower_index == 0:
                is_after_empty = flowerbed[flower_index + 1] == 0

                # Can plant if current and next plots are empty
                if is_current_empty and is_after_empty:
                    flowerbed[flower_index] = 1  # Plant a flower
                    n -= 1  # Decrease required flower count

            # Check for the last plot (another boundary condition)
            elif flower_index == last_index:
                is_before_empty = flowerbed[flower_index - 1] == 0

                # Can plant if current and previous plots are empty
                if is_current_empty and is_before_empty:
                    flowerbed[flower_index] = 1
                    n -= 1

            # Check for plots in the middle
            else:
                is_before_empty = flowerbed[flower_index - 1] == 0
                is_after_empty = flowerbed[flower_index + 1] == 0

                # Can plant if previous, current, and next plots are empty
                if is_before_empty and is_current_empty and is_after_empty:
                    flowerbed[flower_index] = 1
                    n -= 1

        # If we planted all required flowers, return True
        return n <= 0