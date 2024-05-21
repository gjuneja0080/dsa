class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        islands = 0
        visited = set(())
        def bfs(row, col):
            q = deque()
            visited.add((row, col))
            q.append((row, col))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    x, y = r + dr, c + dc
                    if (x in range(len(grid))) and (y in range(len(grid[0]))) and (grid[x][y] == '1') and ((x, y) not in visited):
                        q.append((x, y))
                        visited.add((x, y))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        
        return islands
