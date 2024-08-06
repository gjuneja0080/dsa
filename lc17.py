class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        alphadict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno",
                         "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def backtrack(i, curstr):
            if len(curstr) == len(digits):
                res.append(curstr)
                return

            for char in alphadict[digits[i]]:
                backtrack(i+1, curstr+char)

        backtrack(0, "")
        if len(digits) == 0: return []
        
        return res
