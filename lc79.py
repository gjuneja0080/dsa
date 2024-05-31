class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        rows, cols = len(board), len(board[0])
        def dfs(row, col, ind):
            if ind == len(word):
                return True
            if (row < 0 or col < 0 or (row, col) in path or 
                row > rows - 1 or col > cols - 1 or board[row][col] != word[ind]):
                return False
            
            path.add((row, col))
            res = (dfs(row + 1, col, ind + 1) or
                  dfs(row - 1, col, ind + 1) or
                  dfs(row, col + 1, ind + 1) or
                  dfs(row, col - 1, ind + 1))
            path.remove((row, col))
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                res = dfs(r, c, 0)
                if res: return True
        return False
