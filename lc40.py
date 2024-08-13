class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(nums, ind, target):
            if target == 0:
                res.append(nums[:])
                return
            elif target < 0:
                return
            for i in range(ind, len(candidates)):
                if candidates[i] <= target:
                    if i > ind and candidates[i] == candidates[i-1]:
                        continue
                    nums.append(candidates[i])
                    backtrack(nums, i+1, target - candidates[i])
                    nums.pop()
        candidates.sort()
        backtrack([], 0, target)

        return res
