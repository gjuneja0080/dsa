class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(row, col):
            queue = deque([(row, col)])
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while queue:
                r, c = queue.popleft()
                for x, y in directions:
                    nr, nc = r + x, c + y
                    if (0 <= nr <= rows - 1) and (0 <= nc <= cols - 1) and \
                        (board[nr][nc] == 'O') and ((nr, nc) not in visited):
                        region_dict[region_count].append([nr, nc])
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        visited = set()
        region_count = 1
        region_dict = defaultdict(list)
        rows, cols = len(board), len(board[0])
        for row in range(1, rows-1):
            for col in range(1, cols-1):
                if board[row][col] == 'O' and (row, col) not in visited:
                    region_dict[region_count].append([row, col])
                    visited.add((row, col))
                    bfs(row, col)
                    region_count += 1

        for region in region_dict:
            isValid = True
            for row, col in region_dict[region]:
                if row == len(board) - 1 or row == 0 or col == len(board[0]) - 1 or col == 0:
                    isValid = False
            if isValid:
                for row, col in region_dict[region]:
                    board[row][col] = 'X'
##################################################################################################################

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        def dfs(row, col):
            if row < 0 or col < 0 \
                or row >= rows or col >= cols \
                or board[row][col] != 'O':
                return

            board[row][col] = 'T'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' \
                    and row in (0, rows - 1) \
                    or col in (0, cols - 1):
                    dfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'T':
                    board[row][col] = 'O'
