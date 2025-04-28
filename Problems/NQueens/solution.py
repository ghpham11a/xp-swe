class Solution:
    def solve_n_queens(self, n):
        
        board_template = [['.' for i in range(n)] for row in range(n)]
        results = []
        self.solve_n_queens_recur(n, 0, [], results)
        
        displayed_results = []
        for placements in results:
            board = list(board_template)
            for row_index, col_index in enumerate(placements):
                board[row_index] = list(board[row_index])
                board[row_index][col_index] = 'Q'
                board[row_index] = "".join(board[row_index])
            displayed_results.append(board)

        return displayed_results
        
    def solve_n_queens_recur(self, n, row, col_placements, result):
        if row == n:
            result.append(list(col_placements))
        else:
            for col in range(0, n):
                col_placements.append(col)
                if self.is_valid(col_placements):
                    self.solve_n_queens_recur(n, row + 1, col_placements, result)
                del col_placements[len(col_placements) - 1]
                
    def is_valid(self, col_placements):
        
        row_to_validate = len(col_placements) - 1
        
        for i in range(0, row_to_validate):
            
            abs_col_distance = abs(col_placements[i] - col_placements[row_to_validate])
            
            if abs_col_distance == 0:
                return False
            if abs_col_distance == (row_to_validate - i):
                return False
        
        return True