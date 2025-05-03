class Solution(object):

    def exist(self, board, word):
        # Loop through every cell in the board
        for row_index in range(len(board)):
            for col_index in range(len(board[0])):
                # Start backtracking from cell (row_index, col_index) if it matches the first character
                if self.backtrack(board, row_index, col_index, word):
                    return True  # If a valid path is found, return True

        return False  # If no path matches the word, return False

    def backtrack(self, board, row, col, suffix):
        # Base case: if the entire suffix has been matched
        if len(suffix) == 0:
            return True

        # Check if the current cell is valid and matches the first character of the suffix
        if not self.is_valid(board, row, col, suffix):
            return False

        # Temporarily mark the current cell as visited
        board[row][col] = '#'

        # Try all 4 directions: down, right, up, left
        top_output = self.backtrack(board, row + 1, col, suffix[1:])
        right_output = self.backtrack(board, row, col + 1, suffix[1:])
        bottom_output = self.backtrack(board, row - 1, col, suffix[1:])
        left_output = self.backtrack(board, row, col - 1, suffix[1:])

        # If any direction returns True, the current path is valid
        output = top_output or right_output or bottom_output or left_output

        # Restore the original character in the board (backtracking)
        board[row][col] = suffix[0]

        return output  # Return whether any of the recursive calls succeeded

    def is_valid(self, board, row, col, suffix):
        # Check row and column bounds
        if row < 0 or row >= len(board):
            return False
        if col < 0 or col >= len(board[0]):
            return False

        # Check if the current cell matches the expected character and isn't visited
        if board[row][col] != suffix[0]:
            return False

        return True

solution = Solution()

assert(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True)
assert(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") == False)

print("PASS")