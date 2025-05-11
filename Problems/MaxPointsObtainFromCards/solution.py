from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # `left` marks the start of the window that we slide
        left = 0
        # `right` is the start of the window of size len(cardPoints) - k
        # This window represents the subarray of cards we *don't* take
        right = len(cardPoints) - k

        # Calculate the initial sum by taking all cards from the end
        total = sum(cardPoints[right:])

        # `output` keeps track of the maximum score found so far
        output = total

        # Slide the window one card to the right at a time
        while right < len(cardPoints):
            # Add the card at the current left (we're including it now)
            # Subtract the card at the current right (we're excluding it now)
            total += (cardPoints[left] - cardPoints[right])

            # Update the maximum score
            output = max(output, total)

            # Move the window forward
            left += 1
            right += 1

        return output