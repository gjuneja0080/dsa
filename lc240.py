class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr):
            lp, rp = 0, len(arr) - 1
            while lp <= rp:
                mid = (lp + rp) // 2
                if target > arr[mid]:
                    lp = mid + 1
                elif target < arr[mid]:
                    rp = mid - 1
                else:
                    return True
            return False

        for row in matrix:
            if binary_search(row):
                return True
        return False
############################################################################################################

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        up, rp = rows - 1, 0
        while up > -1 and rp < cols:
            if target > matrix[up][rp]:
                rp += 1
            elif target < matrix[up][rp]:
                up -= 1
            else:
                return True
        return False
