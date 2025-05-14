class Solution:

    def custom_sort_string(self, order, s):
        # Step 1: Build a ranking dictionary
        # 'RANK' assigns each character a priority based on its position in 'order'
        # Characters not in 'order' are assigned a rank based on their first appearance in 's'
        RANK = {}
        for index, char in enumerate(order + s):
            if char not in RANK:
                RANK[char] = index  # Preserve order from 'order' first, then fill from 's'

        # Step 2: Sort the characters in 's' using the custom ranking
        output = sorted(s, key=lambda x: RANK[x])

        # Step 3: Combine sorted characters back into a string
        return "".join(output)