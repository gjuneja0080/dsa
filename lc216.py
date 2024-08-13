class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(ind, nums):
            if n == sum(nums) and len(nums) == k:
                res.append(nums[:])
                return
            if sum(nums) > n:
                return
            for i in range(ind, n):
                if i < 10:
                    backtrack(i + 1, [i] + nums)
        backtrack(1, [])
        return res
