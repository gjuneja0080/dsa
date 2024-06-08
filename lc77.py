class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(ind = 1, lst = []):
            if len(lst) == k:
                res.append(lst[:])
                return
            for i in range(ind, n + 1):
                lst.append(i)
                backtrack(i + 1, lst)
                lst.pop()
        
        res = []
        backtrack()
        return res
