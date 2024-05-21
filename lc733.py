class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image: return
        if image[sr][sc] == color: return image
        
        def bfs(row, col):
            init_col = image[sr][sc]
            q = deque([(row, col)])
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                r, c  = q.popleft()
                for dr, dc in directions:
                    x, y = r + dr, c + dc
                    if (0 <= x < len(image)) and (0 <= y < len(image[0])) and (image[x][y] == init_col):
                        image[x][y] = color
                        q.append((x, y))
        bfs(sr, sc)
        image[sr][sc] = color
        return image
