class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        prev_dir = 'up'
        visited = set()
        row, col = 0, 0
        rows = len(matrix)
        cols = len(matrix[0])

        while len(visited) != (rows * cols):

            if prev_dir == 'up':
                while col < cols:
                    if (row, col) not in visited:
                        res.append(matrix[row][col])
                        visited.add((row, col))
                    if (col < cols - 1) and ((row, col + 1) in visited):
                        prev_dir = 'right'
                        break
                    
                    col += 1
                prev_dir = 'right'
                if col >= cols: col -= 1

            if prev_dir == 'right':
                while row < rows:
                    if (row, col) not in visited:
                        res.append(matrix[row][col])
                        visited.add((row, col))
                    if (row < rows - 1) and ((row + 1, col) in visited):
                        prev_dir = 'down'
                        break
                    row += 1
                prev_dir = 'down'
                if row >= rows: row -= 1

            if prev_dir == 'down':
                while col >= 0:
                    if (row, col) not in visited:
                        res.append(matrix[row][col])
                        visited.add((row, col))
                    if (col > 0) and ((row, col - 1) in visited):
                        prev_dir = 'left'
                        break
                    
                    col -= 1
                prev_dir = 'left'
                if col < 0: col += 1

            if prev_dir == 'left':
                while row >= 0:
                    if (row, col) not in visited:
                        res.append(matrix[row][col])
                        visited.add((row, col))
                    if (row > 0) and ((row - 1, col) in visited):
                        prev_dir = 'up'
                        break
                    
                    row -= 1
                prev_dir = 'up'
                if row < 0: row += 1

        return res
