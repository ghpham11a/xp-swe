from typing import List

class Solution:

    def solve(self, board: List[List[str]]) -> None:
        row_len = len(board)
        col_len = len(board[0])

        # 1. Find and mark unsurrounded 'O' regions (convert 'O' to temporary marker 'T')
        for row in range(row_len):
            for col in range(col_len):
                is_o = board[row][col] == "O"
                is_on_top_or_bottom = (row == 0 or row == row_len - 1)
                is_on_left_or_right = (col == 0 or col == col_len - 1)
                # If the 'O' is on the border, start DFS from here
                if is_o and (is_on_top_or_bottom or is_on_left_or_right):
                    self.dfs(board, row, col)

        # 2. Convert all remaining 'O's (truly surrounded regions) to 'X'
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == "O":
                    board[row][col] = "X"

        # 3. Revert the temporary marker 'T' back to 'O' (unsurrounded regions)
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == "T":
                    board[row][col] = "O"

    def dfs(self, board, row, col):
        # Base case: return if cell is out of bounds or not a valid 'O'
        if not self.is_valid(board, row, col):
            return

        # Temporarily mark the 'O' cell as 'T' to prevent it from being captured
        board[row][col] = "T"

        # Explore all four directions (up, right, down, left)
        self.dfs(board, row - 1, col)
        self.dfs(board, row, col + 1)
        self.dfs(board, row + 1, col)
        self.dfs(board, row, col - 1)

    def is_valid(self, board, row, col):
        # Check for out-of-bounds indices
        if row < 0 or row >= len(board):
            return False
        if col < 0 or col >= len(board[0]):
            return False

        # Only process cells with 'O'
        if board[row][col] != "O":
            return False

        return True

solution = Solution()

test_input_1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solution.solve(test_input_1)
assert(test_input_1 == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])

print("PASS")