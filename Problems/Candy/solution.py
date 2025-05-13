from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:

        # Step 1: Initialize a distribution list where each child gets at least 1 candy
        dist = [1] * len(ratings)
        
        # Step 2: Left-to-right pass
        # If a child has a higher rating than the previous child, give them more candies than the previous child
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                dist[i] = dist[i - 1] + 1

        # Step 3: Right-to-left pass
        # If a child has a higher rating than the next child, make sure they have more candies
        # Use max() to ensure we don't overwrite a larger value assigned from the left-to-right pass
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                dist[i] = max(dist[i], dist[i + 1] + 1)

        # Step 4: Sum up all the candies to get the minimum total needed
        return sum(dist)