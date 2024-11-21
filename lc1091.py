class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1]== 1:
            return -1
        if n == 1:
            return 1 if grid[0][0] == 0 else -1

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 
        queue = deque([(0, 0, 1)])
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while queue:
            row, col, path_length = queue.popleft()

            if row == n - 1 and col == n - 1:
                return path_length

            for dr, dc in directions:

                next_row, next_col = row + dr, col + dc
                if 0 <= next_row < n \
                    and 0 <= next_col < n \
                    and grid[next_row][next_col] == 0 \
                    and not visited[next_row][next_col]:

                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col, path_length + 1))
    
        return -1
        
