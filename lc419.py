class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(row, col):
            if not 0 <= row < rows or not 0 <= col < cols \
               or (row, col) in visited or board[row][col] == '.':
               return

            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        num_ships = 0
        visited = set()
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'X' and (row, col) not in visited:
                    num_ships += 1
                    dfs(row, col)
        return num_ships
