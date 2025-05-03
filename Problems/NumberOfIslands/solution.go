func numIslands(grid [][]byte) int {
    
    result := 0
    
    for row := 0; row < len(grid); row++ {
        for col := 0; col < len(grid[row]); col++ {
            if grid[row][col] == '1' {
                result += 1
                depthFirstSearch(row, col, grid)
            }   
        }
    }
    
    return result
}

func depthFirstSearch(row int, col int, grid [][]byte) {
    
    
    if !isValid(row, col, grid) {
        return
    }
    
    grid[row][col] = '.'
    
    depthFirstSearch(row + 1, col, grid)
    depthFirstSearch(row - 1, col, grid)
    depthFirstSearch(row, col + 1, grid)
    depthFirstSearch(row, col - 1, grid)
    
}

func isValid(row int, col int, grid [][]byte) bool {
    
    if row < 0 || row >= len(grid) {
        return false
    }
    
    if col < 0 || col >= len(grid[row]) {
        return false
    }
    
    if grid[row][col] != '1' {
        return false
    }
    
    return true
    
}
