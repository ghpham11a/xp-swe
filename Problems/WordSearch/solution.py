class Solution(object):
    
    def exist(self, board, word):

        for row_index in range(len(board)):
            for col_index in range(len(board[0])):
                if self.backtrack(board, row_index, col_index, word):
                    return True

        return False

    def backtrack(self, board, row, col, suffix):

        if len(suffix) == 0:
            return True

        if not self.is_valid(board, row, col, suffix):
            return False

        board[row][col] = '#'

        output = False

        top_output = self.backtrack(board, row + 1, col, suffix[1:])
        right_output = self.backtrack(board, row, col + 1, suffix[1:])
        bottom_output = self.backtrack(board, row - 1, col, suffix[1:])
        left_output = self.backtrack(board, row, col - 1, suffix[1:])

        output = top_output or right_output or bottom_output or left_output

        board[row][col] = suffix[0]

        return output

    def is_valid(self, board, row, col, suffix):

        if row < 0 or row >= len(board):
            return False

        if col < 0 or col >= len(board[0]):
            return False

        if board[row][col] != suffix[0]:
            return False

        return True

solution = Solution()

assert(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True)
assert(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") == False)

print("PASS")