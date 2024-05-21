class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        
        onesRow = [0] * rows
        onesCol = [0] * cols
    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    onesRow[row] += 1
                    onesCol[col] += 1
        
        for row in range(rows):
            for col in range(cols):
                grid[row][col] = 2 * onesRow[row] + 2 * onesCol[col] - rows - cols
        
        return grid
