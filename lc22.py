class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(num_open, num_close, paren):
            
            if num_open == num_close == n:
                res.append(paren)
                return
            
            if num_open < n:
                backtrack(num_open + 1, num_close, paren + '(')
            
            if num_close < num_open:
                backtrack(num_open, num_close + 1, paren + ')')
        
        res = []
        backtrack(0, 0, '')
        return res
