class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(row, col):
            visited = ()
            q = deque()
            q.append([row, col, (row, col), 0])
            while q:
                row, col, visited, dist = q.popleft()
                for nr, nc in directions:
                    x, y = row + nr, col + nc
                    if (0 <= x < rows and 0 <= y < cols
                        and rooms[x][y] > 0 and (x, y) not in visited):
                        if rooms[x][y] > dist + 1:
                            rooms[x][y] = dist + 1
                            q.append([x, y, (x, y), dist + 1])

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    bfs(row, col)
