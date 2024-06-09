class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(word):
            lp, rp = 0, len(word) - 1
            while lp < rp:
                if word[lp] != word[rp]:
                    return False
                lp += 1
                rp -= 1
            return True

        def backtrack(ind, lst):
            if ind >= len(s):
                res.append(lst[:])
                return
            for i in range(ind, len(s)):
                if isPalin(s[ind:i + 1]):
                    lst.append(s[ind:i + 1])
                    backtrack(i + 1, lst)
                    lst.pop()
        res = []
        backtrack(0, [])

        return res
