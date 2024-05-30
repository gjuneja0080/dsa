class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]: return 0
        rows, cols = len(grid), len(grid[0])
        
        dp = [[0]*cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        
        # first row only
        for col in range(1, cols):
            dp[0][col] = dp[0][col-1] + grid[0][col]
        
        #first col only
        for row in range(1, rows):
            dp[row][0] = dp[row-1][0] + grid[row][0]
        
        # rest of the matrix
        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]

        return dp[rows-1][cols-1]
