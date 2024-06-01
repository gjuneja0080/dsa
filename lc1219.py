class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(row, col, path):
            if (min(row, col) < 0 or 
                row == rows or col == cols or 
                (row, col) in path or grid[row][col] == 0):
                return 0

            ans = 0
            path.add((row, col))
            total_gold = grid[row][col] + max(dfs(row + 1, col, path), 
                                        dfs(row - 1, col, path), 
                                        dfs(row, col + 1, path), 
                                        dfs(row, col - 1, path))

            path.remove((row, col))
            return total_gold

        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, set()))
        return res
