class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_min, global_max, max_diff = arrays[0][0], arrays[0][-1], 0
        for i in range(1, len(arrays)):
            current_min, current_max = arrays[i][0], arrays[i][-1]
            max_diff = max(max_diff, abs(global_max - current_min), abs(current_max - global_min))
            global_min = min(global_min, current_min)
            global_max = max(global_max, current_max)
        
        return max_diff
