class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][cols - 1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if top > bot:
            return False
        lp, rp = 0, cols-1
        matrow = matrix[row]
        while lp <= rp:
            mid = (lp + rp) // 2
            if target > matrow[mid]:
                lp = mid + 1
            elif target < matrow[mid]:
                rp = mid - 1
            else:
                return True
        return False
