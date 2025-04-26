class Solution:

    def spiral_order(self, matrix):
        result = []  # List to store the elements in spiral order.
        
        rows, columns = len(matrix), len(matrix[0])  # Get number of rows and columns.
        
        # Initialize pointers to track the current boundaries of the spiral.
        up = left = 0
        right = columns - 1
        down = rows - 1

        # Continue looping until we have collected all elements.
        while len(result) < rows * columns:
            # Traverse from left to right across the top row.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards along the rightmost column.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Check if there is more than one row remaining to avoid double-counting.
            if up != down:
                # Traverse from right to left across the bottom row.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Check if there is more than one column remaining to avoid double-counting.
            if left != right:
                # Traverse upwards along the leftmost column.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            # Move the boundaries inward for the next layer of the spiral.
            left += 1
            right -= 1
            up += 1
            down -= 1

        return result