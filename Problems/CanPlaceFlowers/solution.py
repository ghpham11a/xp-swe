class Solution:
    def canPlaceFlowers(self, flowerbed, n):

        if len(flowerbed) == 1:
            return n <= 0 or flowerbed[0] == 0

        last_index = len(flowerbed) - 1

        for flower_index in range(len(flowerbed)):

            is_current_empty = flowerbed[flower_index] == 0

            if flower_index == 0:
                is_after_empty = flowerbed[flower_index + 1] == 0

                if is_current_empty and is_after_empty:
                    flowerbed[flower_index] = 1
                    n -= 1

            elif flower_index == last_index:
                is_before_empty = flowerbed[flower_index - 1] == 0

                if is_current_empty and is_before_empty:
                    flowerbed[flower_index] = 1
                    n -= 1

            else:
                is_before_empty = flowerbed[flower_index - 1] == 0
                is_after_empty = flowerbed[flower_index + 1] == 0

                if is_before_empty and is_current_empty and is_after_empty:
                    flowerbed[flower_index] = 1
                    n -= 1

        return n <= 0