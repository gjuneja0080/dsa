class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(row, col):
            area = 0
            q = deque([(row, col)])
            visited.add((row, col))
            while q:
                r, c = q.popleft()
                area += 1
                for nr, nc in directions:
                    x, y = r + nr, c + nc
                    if (0 <= x < rows
                        and 0 <= y < cols
                        and (x, y) not in visited
                        and grid[x][y] == 1):
                        visited.add((x, y))
                        q.append((x, y))
            return area
        
        max_area = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, bfs(row, col))

        return max_area
