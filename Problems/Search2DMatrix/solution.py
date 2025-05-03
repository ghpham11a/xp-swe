from typing import List

class Solution:
    
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        # Start at the top-right corner of the matrix
        row = 0
        col = len(matrix[0]) - 1

        # Continue the search while the row is within bounds and the column is not less than 0
        while row < len(matrix) and col >= 0:
            # If the current element matches the target, return True
            if matrix[row][col] == target:
                return True
            # If the current element is greater than the target, move left to a smaller value
            elif matrix[row][col] > target:
                col -= 1
            # If the current element is less than the target, move down to a larger value
            else:
                row += 1

        # If the loop completes without finding the target, return False
        return False