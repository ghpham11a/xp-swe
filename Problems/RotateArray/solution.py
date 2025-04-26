class Solution(object):

    def rotate(self, matrix):
        # Get the size (number of rows, assuming it's a square matrix)
        row_len = len(matrix)
    
        # Step 1: Transpose the matrix
        # Swap matrix[i][j] with matrix[j][i] for all i < j
        # This flips the matrix over its diagonal
        for i in range(0, row_len):
            for j in range(i, row_len):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp

        # Step 2: Reverse each row
        # After transposing, reversing each row results in a 90-degree clockwise rotation
        for i in range(0, row_len):
            for j in range(0, (row_len // 2)):
                # Swap elements from left and right ends of the row
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][row_len - j - 1]
                matrix[i][row_len - j - 1] = tmp

        return matrix