class Solution:

    def custom_sort_string(self, order, s):

        RANK = {}
        for index, char in enumerate(order + s):
            if char not in RANK:
                RANK[char] = index

        output = sorted(s, key=lambda x: RANK[x])

        return "".join(output)