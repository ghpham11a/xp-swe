class Solution(object):

    def solve(self, board):

        row_len = len(board)
        col_len = len(board[0])
        
        # 1. Capture unsurrounded regions (O -> T)
        for row in range(row_len):
            for col in range(col_len):
                is_o = board[row][col] == "O"
                is_on_top_or_bottom = (row == 0 or row == row_len - 1)
                is_on_left_or_right = (col == 0 or col == col_len - 1)
                if is_o and (is_on_top_or_bottom or is_on_left_or_right):
                    self.dfs(board, row, col)

        # 2. Capture surrounded regions (O -> X)
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == "O":
                    board[row][col] = "X"

        # 3. Uncapture surrounded regions (T -> O)
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == "T":
                    board[row][col] = "O"

    def is_valid(self, board, row, col):
        if row < 0 or row >= len(board):
            return False

        if col < 0 or col >= len(board[0]):
            return False

        if board[row][col] != "O":
            return False

        return True

    def dfs(self, board, row, col):
        
        if not self.is_valid(board, row, col):
            return

        board[row][col] = "T"

        self.dfs(board, row - 1, col)
        self.dfs(board, row, col + 1)
        self.dfs(board, row + 1, col)
        self.dfs(board, row, col - 1)

solution = Solution()

test_input_1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solution.solve(test_input_1)
assert(test_input_1 == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])

print("PASS")