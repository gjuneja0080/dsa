class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_oranges = 0
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        if fresh_oranges == 0: return 0

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            found_fresh = False
            for _ in range(len(queue)):  
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        found_fresh = True
                        queue.append((nr, nc))
            if found_fresh:
                minutes += 1

        return minutes if fresh_oranges == 0 else -1
